from django.urls import path
from accounts.views import UserRegistrations
from accounts import views

urlpatterns = [

    path('', views.AccountLogin,name='login'),
    path('home/',views.AccountHome,name='home'),
    path('registration/',UserRegistrations.as_view(),name='registration'),
    path('userlogin/',views.User_login, name='userlogin'),
    path('userlogout/',views.UserLogout, name='userlogout'),

]
