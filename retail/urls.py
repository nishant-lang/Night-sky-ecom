
from django.urls import path
from retail import views
from retail.views import AddProduct,FiltersProducts


urlpatterns = [
    path('',views.Retailhome,name='retailhome'),
    path('addproduct/', AddProduct.as_view(), name='registrations'),
    path('filterproduct/<uuid:id', FiltersProducts.as_view(), name='filterproduct'),
]

