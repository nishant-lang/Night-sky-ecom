
from rest_framework import serializers
from accounts.models import User

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
        
        