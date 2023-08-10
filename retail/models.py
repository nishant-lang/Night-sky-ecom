from django.db import models
from accounts.models import User
# Create your models here.


class ProductCatogory(models.Model):
    category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category

class Product(models.Model):
    category=models.ForeignKey(ProductCatogory,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name=models.CharField(max_length=100)
    product_pic= models.FileField(upload_to='produc_item')
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='last_updated_by')
    last_updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
 

    