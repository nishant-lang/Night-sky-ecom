from django.db import models
from accounts.models import User
from django.utils.text import slugify
import random
import string

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
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # unique_identifier = f"{self.name}-{self.desc[:10]}"
            # self.slug = slugify(unique_identifier)
            random_word = ''.join(random.choices(string.ascii_letters, k=6))  # Generate a random word of length 6
            unique_identifier = f"{self.name}-{self.desc[:10]}-{random_word}"
            self.slug = slugify(unique_identifier)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
 

   

