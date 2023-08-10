from django.shortcuts import render
from retail.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def BayerHome(request):
    obj=Product.objects.all()
    return render(request,'bayer/home.html',{'obj':obj})
    