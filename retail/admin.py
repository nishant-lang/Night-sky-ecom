from django.contrib import admin
from retail.models import Product,ProductCatogory

# Register your models here.


@admin.register(ProductCatogory)
class AdminUser(admin.ModelAdmin):
    list_display = ('id','category')

@admin.register(Product)
class AdminUser(admin.ModelAdmin):
    list_display = ('id','category','product_pic','name','price','desc','datetime')