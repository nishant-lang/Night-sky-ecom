from django.shortcuts import render
from retail.models import Product,ProductCatogory
from rest_framework.views import APIView
from retail.serializers import AddProductserializers
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

def Retailhome(request):
    # obj=Product.objects.all()
    user=request.user
    objs=ProductCatogory.objects.all()
    products=Product.objects.filter(user=user)
    print(products)

    return render(request,'retail/home.html',{'objs':objs,'products':products})


# API FOR ADD THE PRODUCT

class AddProduct(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self,request):
        serializer=AddProductserializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # print(user)
            return Response({"message": "Your Product has been Added"})
        else:
            return Response(serializer.errors, status=400)
        