from django.db import models
from accounts.models import User
from django.utils.text import slugify
import random
import string
import uuid
from django.contrib.auth.models import User


# Create your models here.


class ProductCatogory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category



from django.conf import settings

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(ProductCatogory, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Corrected
    name = models.CharField(max_length=100)
    product_pic = models.FileField(upload_to='product_item')
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    user_cart = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='cart_products')  # Corrected

    # Stripe fields
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.name





    def save(self, *args, **kwargs):

        if not self.slug:
            random_word = ''.join(random.choices(string.ascii_letters, k=6)) 
            unique_identifier = f"{self.name}-{self.desc[:10]}-{random_word}"
            self.slug = slugify(unique_identifier)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
 

   

