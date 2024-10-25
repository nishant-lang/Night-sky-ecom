from django.shortcuts import render
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import RegistrationsSerializers,SendPasswordResetEmailSerializer,UserPasswordResetSerializer
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from rest_framework import status


def AccountHome(request):
    csrf_token = get_token(request)
    context = {
        'csrf_token': csrf_token,
    }

    return render(request,'accounts/home.html',context)

def AccountLogin(request):

    csrf_token = get_token(request)
    context = {
        'csrf_token': csrf_token,
    }
    
    return render(request,"accounts/login.html",context)



# Create your views here.
class UserRegistrations(APIView):

    def post(self,request):

        serializer=RegistrationsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":" Your Registration Successfull"},status=200,)
        else:
            if 'non_field_errors' in serializer.errors:
                return Response({'regd_pass_errors':serializer.errors['non_field_errors'][0]},status=400)
            else:
                if 'email' in serializer.errors:
                   return Response(serializer.errors,status=400)
                #    return Response( serializer.errors['email'],status=400)
                if 'username' in serializer.errors:
                   return Response(serializer.errors,status=400)
                    # return Response( serializer.errors['username'],status=400)
                if 'gender' in serializer.errors:
                   return Response(serializer.errors,status=400)
                    # return Response( serializer.errors['gender'],status=400)
                if 'password' in serializer.errors:
                   return Response(serializer.errors,status=400)
                    # return Response( serializer.errors['password'],status=400)
                if 'password2' in serializer.errors:
                   return Response(serializer.errors,status=400)
                    # return Response( serializer.errors['password2'],status=400)
                return Response(serializer.errors,status=400)


def User_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)
       
        if not email:
            messages.error(request, 'You must Enter email.')
            return redirect('/')

        if not password:
            messages.error(request, 'You must Enter Password.')
            return redirect('/')

        if email and password: 
            # print('helllooo')
            user = authenticate(request, email=email.lower(), password=password)
            # print(user)
            if user is not None:
                if user.is_retailer:
                
                    context={
                        'user':user,
                    }
                    login(request, user)
                    messages.success(request, 'You have been logged in successfully.')
                    return redirect('/retail/',context)
                    # return render(request,'retail/home.html',context)
                else:
                    context={
                        'user':user,
                    }
                    login(request, user)
                    messages.success(request, 'You have been logged in successfully.')
                    return redirect('/bayer/',context)
            else:
                messages.error(request, 'Authentication failed. Please check your credentials.')
        return redirect('/')
    else:
        return redirect('/')



def UserLogout(request):
    logout(request)
    return redirect('/')
   

def Forgot_password_email(request):
    csrf_token = get_token(request)
    context = {
        'csrf_token': csrf_token,
    }
    return render(request,'accounts/forgot-password.html',context)

def Password_reset(request,uid,token):
    csrf_token = get_token(request)

    context={
        'uid':uid,
        'token':token,
        'csrf_token':csrf_token
    }

    return render(request,'accounts/resetpass.html',context)


class SendPasswordResetEmailView(APIView):
    print('this api hits')

    def post(self,request,format=None):
        serializer=SendPasswordResetEmailSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset link sent.Pease check your Email.'},status.HTTP_200_OK)
        if 'non_field_errors' in serializer.errors:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    

class UserPasswordResetView(APIView):

    def post(self,request,uid,token,format=None):
        print(uid)
        print(token)
        serializer=UserPasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})

        if serializer.is_valid(raise_exception=True):
            return Response({'Msg':'Password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)