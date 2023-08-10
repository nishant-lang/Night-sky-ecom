from django.contrib import admin
from retail.models import Product,ProductCatogory
# Register your models here.

   
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user', 'price', 'desc','last_updated_by','last_updated_at' ,'datetime')
    list_filter = ('category', 'user')
    search_fields = ('name', 'desc')
    list_per_page = 20

    def save_model(self, request, obj):
       
        obj.last_updated_by = request.user
        obj.save()

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCatogory)


    


