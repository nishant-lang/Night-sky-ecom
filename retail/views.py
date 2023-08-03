from django.shortcuts import render
from retail.models import Product
from rest_framework.views import APIView
from retail.serializers import AddProductserializers
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

def Retailhome(request):
    obj=Product.objects.all()
    return render(request,'retail/home.html',{'obj':obj})


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
        