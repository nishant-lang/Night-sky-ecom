from django.shortcuts import render
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import RegistrationsSerializers
from django.middleware.csrf import get_token
from django.contrib import messages


def AccountHome(request):
    csrf_token = get_token(request)
    context = {
        'csrf_token': csrf_token,
    }
    return render(request,'accounts/home.html',context)

def AccountLogin(request):
    return render(request,"accounts/login.html")


# Create your views here.
class UserRegistrations(APIView):

    def post(self,request):
        # print(request.data)
        serializer=RegistrationsSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # print(user)

            return Response({"message":"User created successfully."},status=200,)
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



