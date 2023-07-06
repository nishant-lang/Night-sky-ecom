from django.urls import path
from accounts.views import UserRegistrations,AccountLogin
from accounts import views

urlpatterns = [
    path('',views.AccountHome,name='bayerhome'),
    path('login/', views.AccountLogin, name='login'),
    path('registration/', UserRegistrations.as_view(), name='registration'),
]
