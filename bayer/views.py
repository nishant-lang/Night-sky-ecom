from django.shortcuts import render
from retail.models import Product
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from permission import IsOwnerOrReadOnly  
from django.middleware.csrf import get_token

@login_required
def BayerHome(request):
    obj=Product.objects.all()
    
    return render(request,'bayer/home.html',{'obj':obj})

@login_required
def CardDetail(request,slug):
    csrftoken = get_token(request)
    
    obj=Product.objects.filter(slug=slug).first()

    context={
        'obj':obj,
        'csrftoken':csrftoken
    }

    print(obj.name)
    print(obj.price)

    return render(request,"bayer/card.html",context)


def CartDetail(request):
   

    return render(request,"bayer/cart.html")

@api_view(['POST'])
# @permission_classes([IsAuthenticated, IsOwnerOrReadOnly])  # Use the custom permission class
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    request.user.cart_products.add(product)
    return Response({'message': 'Product added to cart successfully.'})

@api_view(['POST'])
# @permission_classes([IsAuthenticated, IsOwnerOrReadOnly])  # Use the custom permission class
def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    request.user.cart_products.remove(product)
    return Response({'message': 'Product removed from cart successfully.'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def view_cart(request):
    cart_products = request.user.cart_products.all()
    # You can customize the response format as needed
    cart_data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in cart_products]
    return Response(cart_data)