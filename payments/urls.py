from django.urls import path
from .views import create_checkout_session,stripe_webhook,payment_success,payment_cancel

urlpatterns = [
    # path('checkout/', checkout_page, name='checkout_page'), 
    path('create-checkout-session/<uuid:product_id>/', create_checkout_session, name='create_checkout_session'),
    path("stripe-webhook/", stripe_webhook, name="stripe_webhook"),
    path("success/", payment_success, name="payment_success"),
    path("cancel/", payment_cancel, name="payment_cancel"),
    
    
]
