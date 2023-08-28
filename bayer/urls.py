
from django.urls import path
from bayer import views

urlpatterns = [
  
    path('', views.BayerHome,name='bayerhome'),
    path("card_detail/<slug:slug>",views.CardDetail,name='card_detail'),
]
