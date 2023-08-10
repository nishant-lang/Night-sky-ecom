
from django.urls import path
from bayer import views

urlpatterns = [
  
    path('', views.BayerHome,name='bayerhome'),
]
