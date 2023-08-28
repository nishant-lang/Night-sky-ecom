from django.shortcuts import render
from retail.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def BayerHome(request):
    obj=Product.objects.all()
    print
    return render(request,'bayer/home.html',{'obj':obj})

def CardDetail(request,slug):
    print(slug)
    obj=Product.objects.filter(slug=slug).first()
    print(obj.name)
    print(obj.price)
    return render(request,"bayer/card.html")