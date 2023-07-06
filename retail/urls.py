
from django.urls import path
from retail import views
from retail.views import AddProduct

urlpatterns = [
  
    path('',views.Retailhome,name='retailhome'),
    path('addproduct/', AddProduct.as_view(), name='registrations'),
]
