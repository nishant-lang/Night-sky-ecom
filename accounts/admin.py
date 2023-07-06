from django.contrib import admin
from accounts.models import User
from django.contrib import admin
# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('id','email','username','state','city','pincode','gender','is_staff','is_retailer','is_active')

