from rest_framework import serializers
from retail.models import Product,ProductCatogory


class ProductCatogorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatogory
        fields = ['category']


class AddProductserializers(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCatogory.objects.all())
    name=serializers.CharField()
    product_pic=serializers.FileField()
    price=serializers.CharField()
    desc=serializers.CharField()
    
    def create(self, validated_data):

        product_pic=validated_data.get('product_pic')
        category=validated_data.get('category')
        name=validated_data['name']
        price=validated_data['price']
        desc=validated_data['desc']
        
        
        product = Product.objects.create(product_pic=product_pic,category=category,name=name,price=price,desc=desc) 
        
        return product
