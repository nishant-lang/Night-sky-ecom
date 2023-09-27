from django.shortcuts import render
from retail.models import Product,ProductCatogory
from rest_framework.views import APIView
from retail.serializers import AddProductSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from django.middleware.csrf import get_token
from django.db.models import Q

# Create your views here.

def Retailhome(request):
    objs = ProductCatogory.objects.all()
    
    csrftoken = get_token(request)
    # print(csrftoken)
    products=Product.objects.filter(user=request.user).order_by('-id')
    # print(products)
    
    context={
       'products':products,
       'csrftoken':csrftoken,
       'objs':objs
    }
    return render(request,'retail/home.html',context) 


# API FOR ADD THE PRODUCT

class AddProduct(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request):
        context={
            'user':request.user
        }
        serializer=AddProductSerializer(data=request.data,context=context)
    
        if serializer.is_valid():
            serializer.save()

            return Response({"message":"Your Product has been Added"})
        else:
            return Response(serializer.errors, status=400)
    

class FiltersProducts(APIView):
    def get(self,request,id):

        related_products = Product.objects.filter(Q(category_id=id) & Q(user=request.user))
        serializer = ProductSerializer(related_products, many=True)
        
        return Response(serializer.data)
        


