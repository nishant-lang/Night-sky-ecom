from django.urls import path
from accounts.views import UserRegistrations,SendPasswordResetEmailView,UserPasswordResetView
from accounts import views

urlpatterns = [

    path('', views.AccountLogin,name='login'),
    path('home/',views.AccountHome,name='home'),
    path('registration/',UserRegistrations.as_view(),name='registration'),
    path('userlogin/',views.User_login, name='userlogin'),
    path('userlogout/',views.UserLogout, name='userlogout'),
    path('forgot-password/',views.Forgot_password_email, name='forgot_password'),
    path('reset-link-page/<uid>/<token>',views.Password_reset, name='password_reset'),
    

    
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),

]
