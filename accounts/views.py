from django.shortcuts import render
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import RegistrationsSerializers,UserLoginSerializer
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.serializers import UserLoginSerializer
from django.contrib import messages
from django.contrib.auth import logout

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
        
        if not email:
            messages.error(request, 'You must Enter email.')
            return redirect('/')

        if not password:
            messages.error(request, 'You must Enter Password.')
            return redirect('/')

        if email and password: 
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in successfully!')
                return redirect('/retail/')
            else:
                messages.error(request, 'Authentication failed. Please check your credentials.')
        return redirect('/')

    else:
        # return render(request, 'accounts/login.html')
        return redirect('/')



def UserLogout(request):
    logout(request)
    return redirect('/')
