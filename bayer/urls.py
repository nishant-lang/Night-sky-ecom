
from django.urls import path
from bayer import views

urlpatterns = [
  
    path('', views.BayerHome,name='bayerhome'),
    path("card_detail/<slug:slug>",views.CardDetail,name='card_detail'),
    
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('remove-cart-product/<uuid:id>/', views.remove_cart_product, name='remove_cart_product'),

    path('user-cart-detail/', views.CartDetail, name='user_cart_detail'),
    path('user-cart/', views.view_cart, name='user_cart'),
    path('remove-cart-product/<uuid:product_id>', views.remove_from_cart, name='remove_cart_product'),

]
