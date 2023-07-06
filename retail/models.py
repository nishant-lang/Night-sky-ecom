from django.db import models

# Create your models here.


class ProductCatogory(models.Model):
    category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category


class Product(models.Model):
    category=models.ForeignKey(ProductCatogory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    product_pic= models.FileField(upload_to='produc_item')
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
 

    