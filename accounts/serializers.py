
from rest_framework import serializers
from accounts.models import User
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from accounts.utils import Util

class RegistrationsSerializers(serializers.Serializer):
        
        # email = serializers.EmailField(error_messages={'blank': 'email is require.'})
        email = serializers.EmailField()
        username=serializers.CharField()
        gender=serializers.CharField()
        state=serializers.CharField()
        city=serializers.CharField()
        pincode=serializers.CharField()
        is_retailer=serializers.BooleanField(default=False)
        password = serializers.CharField(write_only=True,required=True)
        password2 = serializers.CharField(write_only=True, required=True)


        def validate(self, attrs):
            email = attrs.get('email')
            password = attrs.get('password')
            password2 = attrs.get('password2')
            
            if password and password2 and password != password2:
                raise serializers.ValidationError("Passwords does not match.")

            if User.objects.filter(email=email.lower()).exists():
                raise serializers.ValidationError('You are already registered.')
            
            return attrs

       
        def create(self, validated_data):
            
            email = validated_data.get('email')
            username = validated_data.get('username')
            state=validated_data['state']
            city=validated_data['city']
            gender=validated_data['gender']
            # print(gender)
            pincode=validated_data['pincode']
            # print(pincode)
            is_retailer=validated_data['is_retailer']
            password = validated_data.get('password')
            
            user = User.objects.create_user(email=email,username=username,gender=gender,state=state,city=city,pincode=pincode,is_retailer=is_retailer,password=password) 
            
            return user
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            return data
        
        else:
            raise serializers.ValidationError("Both email and password are required.")
        
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        fields=['email']

    def validate(self, attrs):
        email=attrs.get('email')

        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded Uid',uid)
            token=PasswordResetTokenGenerator().make_token(user)
            print('password Reset Token',token)
            link='http://127.0.0.1:8000/reset-link-page/'+uid+'/'+token

            print('password Reset link',link)
            
            body='Click Following Link to Reset Your password:' +link

            data={
                'subject':'Reset your Password.',
                'body':body,
                'to_email':user.email,
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationError('You do not have a registered user account.')
        


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields=['password','password2']

    def validate(self, attrs):

        try:
            password=attrs.get('password')
            password2=attrs.get('password2')
            uid=self.context.get('uid')
            token=self.context.get('token')

            if password!=password2:
                raise serializers.ValidationError("The Password and Confirm Password do not match.")
            id=smart_str(urlsafe_base64_decode(uid))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):

                raise ValidationError('Token is not valid or Expired.')
            
            user.set_password(password)
            user.save()
            return attrs
        
        except DjangoUnicodeDecodeError as identifire:
            PasswordResetTokenGenerator().check_token(user,token)
            raise ValidationError('Token is not valid or Expired.')