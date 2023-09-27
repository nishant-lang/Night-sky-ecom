
from django.urls import path
from bayer import views

urlpatterns = [
  
    path('', views.BayerHome,name='bayerhome'),
    path("card_detail/<slug:slug>",views.CardDetail,name='card_detail'),
    # path("add-to-cart/<slug:slug>/", views.add_to_cart, name='add-to-cart'),
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('user-cart-detail/', views.CartDetail, name='user-cart-detail'),

]
