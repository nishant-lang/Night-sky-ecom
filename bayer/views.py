from django.shortcuts import render
from retail.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def BayerHome(request):
    obj=Product.objects.all()
    
    return render(request,'bayer/home.html',{'obj':obj})

@login_required
def CardDetail(request,slug):
    
    obj=Product.objects.filter(slug=slug).first()

    context={
        'obj':obj
    }

    print(obj.name)
    print(obj.price)
    
    return render(request,"bayer/card.html",context)