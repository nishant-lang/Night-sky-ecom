from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):

    """Manager for the user"""   
    def create_user(self,email,username,gender,city=None,state=None,pincode=None,password=None,is_retailer=None):
        """Create new user"""
        if not email:
            raise ValueError('User must have the email')
        email=self.normalize_email(email)    
        user=self.model(email=email.lower(),username=username,gender=gender,city=city,state=state,is_retailer=is_retailer,pincode=pincode
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,username,email,password=None):
        """Create a new super user super user"""
        if not email:
            raise ValueError('User must have the email')
        
        email=self.normalize_email(email)
        user=self.model(email=email.lower(),username=username)
        user.set_password(password)
        user.is_superuser=True
        user.is_staff=True
        user.set_password(password)
        user.save(using=self._db)
        return user

                
class User(AbstractBaseUser,PermissionsMixin):
    """data base model for the user """

    email=models.EmailField(max_length=50,unique=True)
    username=models.CharField(max_length=50)
    # fullname=models.models.CharField (max_length=50)
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField()
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False,null=True)
    is_retailer=models.BooleanField(default=False,null=True)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.username
        
 


