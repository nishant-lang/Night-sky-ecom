
import stripe
import logging
from django.conf import settings
from retail.models import Product 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django_ratelimit.decorators import ratelimit
from accounts.models import User




stripe.api_key = settings.STRIPE_SECRET_KEY  # Load Stripe API key


def get_or_create_stripe_price(product):
    """Retrieve or create a Stripe price while handling product name and price updates."""
    
    # If product does not have a Stripe product ID, create one
    if not product.stripe_product_id:
        stripe_product = stripe.Product.create(name=product.name)
        product.stripe_product_id = stripe_product.id
        product.save()

    else:
        # Fetch existing Stripe product and update name if needed
        stripe_product = stripe.Product.retrieve(product.stripe_product_id)

        if stripe_product.name != product.name:  # If name changed, update in Stripe
            stripe.Product.modify(product.stripe_product_id, name=product.name)

    # Convert price to paise (Stripe uses the smallest currency unit)
    unit_amount = int(product.price * 100)

    # If price already exists in DB, check if it's still valid
    if product.stripe_price_id:
        stripe_price = stripe.Price.retrieve(product.stripe_price_id)
        if stripe_price.unit_amount == unit_amount and stripe_price.currency == "inr":
            return product.stripe_price_id  # Reuse existing price
    
    # If price is different, create a new price
    stripe_price = stripe.Price.create(
        unit_amount=unit_amount,
        currency="inr",
        product=product.stripe_product_id,
    )

    # Save the new price ID in the database
    product.stripe_price_id = stripe_price.id
    product.save()

    return stripe_price.id



def get_or_create_stripe_customer(user):
    """Retrieve an existing Stripe customer or create a new one."""

    if user.is_authenticated:

        email = user.email
        # Check if customer exists in Stripe
        existing_customers = stripe.Customer.list(email=email).data

        if existing_customers:
            return existing_customers[0].id  # Return the first matched customer ID

        # Create a new customer if not found
        customer = stripe.Customer.create(
            name=user.get_full_name(),
            email=email,
        )
        return customer.id

    # For guest users, create a new customer (or handle it differently)
    guest_customer = stripe.Customer.create(
        name="Guest",
        email="guest@example.com",
    )
    return guest_customer.id



def handle_successful_payment(session, user_id, product_id):
    '''Create order accoroding to payment'''

    user = None
    if user_id != "guest":
        user = User.objects.get(id=user_id)  # Get the user from DB

    product = Product.objects.get(id=product_id)  # Get the purchased product

    print('product:',product)


    #  🛒 Create an order in the database

    # Order.objects.create(
    #     user=user,
    #     product=product,
    #     price=session["amount_total"] / 100,  # Convert from cents
    #     payment_status="Paid",
    #     stripe_payment_id=session["payment_intent"]
    # )

    print(f"✅ Order created: {user} purchased {product} for ₹{session['amount_total'] / 100}")


import os
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")

logger = logging.getLogger(__name__)

@csrf_exempt
def stripe_webhook(request):

    # print('webhook runing...')
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = STRIPE_WEBHOOK_SECRET 

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        logger.info(f"Received event: {event['type']}")
        
    except ValueError:
        logger.error("Invalid payload")
        return JsonResponse({"error": "Invalid payload"}, status=400)

    
    except stripe.error.SignatureVerificationError:
        logger.error("Invalid signature")
        return JsonResponse({"error": "Invalid signature"}, status=400)

    if event["type"] == "checkout.session.completed":

        session = event["data"]["object"]
        user_id = session.get("metadata", {}).get("user_id", "guest")
        product_id = session.get("metadata",{}).get("product_id")

        handle_successful_payment(session, user_id, product_id)
    
    # print('status": "web hoook success')
    return JsonResponse({"status": "success"}, status=200)



# Load Stripe Secret Key from settings

YOUR_DOMAIN = "http://localhost:8000"  # Change to your actual domain

# Define your domain
# For production use it
# YOUR_DOMAIN = settings.SITE_URL  # Store domain in settings.py


@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def create_checkout_session(request, product_id):
    if request.method == "POST":
        try:
            if not request.user.is_authenticated:
                return JsonResponse({"error": "Authentication required"}, status=403)
            
            product = get_object_or_404(Product, id=product_id)

            price_id = get_or_create_stripe_price(product)

            if not price_id:
                return JsonResponse({"error": "Stripe price ID not found"}, status=400)

            customer_id = get_or_create_stripe_customer(request.user)

            checkout_session = stripe.checkout.Session.create(

                payment_method_types=["card"],
                customer=customer_id,
                line_items=[{
                    "price": price_id,
                    "quantity": 1,
                }],
                mode="payment",
                billing_address_collection="required",
                success_url=f"{YOUR_DOMAIN}/payment/success/",
                cancel_url=f"{YOUR_DOMAIN}/payment/cancel/",

                metadata={  # Add metadata for webhook processing
                "user_id": request.user.id if request.user.is_authenticated else "guest",
                "product_id": product_id,
                }
            )
            return HttpResponseRedirect(checkout_session.url)

        except stripe.error.CardError:
            logger.warning(f"Card declined: {str(e)}")
            return JsonResponse({"error": "Your card was declined. Please try another payment method."}, status=400)

        except stripe.error.RateLimitError:
            logger.error("Too many requests.")
            return JsonResponse({"error": "Too many requests. Please try again later."}, status=429)

        except stripe.error.InvalidRequestError:
            logger.error(f"Invalid request to Stripe: {str(e)}")  # ERROR
            return JsonResponse({"error": "Invalid payment request. Please contact support."}, status=400)

        except stripe.error.AuthenticationError:
            
            return JsonResponse({"error": "Authentication with Stripe failed. Please try again later."}, status=401)

        except stripe.error.APIConnectionError:
            return JsonResponse({"error": "Network error. Please try again later."}, status=502)

        except stripe.error.StripeError:
            logger.critical(f"Stripe API issue: {str(e)}") 
            return JsonResponse({"error": "Payment processing failed. Please try again."}, status=400)

        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            return JsonResponse({"error": "An unexpected error occurred. Please try again later."}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)



def payment_success(request):
    return render(request, "payments/success.html")  # Create this template



def payment_cancel(request):
    return render(request, "payments/cancel.html")  # Create this 




