from rest_framework import serializers
from retail.models import Product,ProductCatogory 
from accounts.models import User 
from django.utils import timezone


class ProductCatogorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatogory
        fields = ['category']


# class AddProductserializers(serializers.Serializer):
#     category = serializers.PrimaryKeyRelatedField(queryset=ProductCatogory.objects.all())
#     name=serializers.CharField()
#     product_pic=serializers.FileField()
#     price=serializers.CharField()
#     desc=serializers.CharField()
#     user=serializers.CharField()
#     last_updated_by=serializers.CharField()
#     last_updated_at=serializers.DateTimeField()
   

#     def create(self, validated_data):
#         product_pic=validated_data.get('product_pic')
#         category=validated_data.get('category')
#         name=validated_data['name']
#         price=validated_data['price']
#         desc=validated_data['desc']
#         user=validated_data['user']
#         last_updated_by=validated_data['last_updated_by']
#         last_updated_at=validated_data['last_updated_at']
        

#         product = Product.objects.create(name=name,product_pic=product_pic,price=price,desc=desc,category=category,user=user,last_updated_by=last_updated_by,last_updated_at=last_updated_at) 
        
#         return product


class AddProductSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCatogory.objects.all())
    name = serializers.CharField()
    product_pic = serializers.FileField()
    price = serializers.CharField()
    desc = serializers.CharField()


    def create(self, validated_data):
        user = self.context['user']
        # print(user)

        product = Product.objects.create(
            category=validated_data['category'],
            name=validated_data['name'],
            product_pic=validated_data['product_pic'],
            price=validated_data['price'],
            desc=validated_data['desc'],
            user=user)
        return product
