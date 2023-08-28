from rest_framework import serializers
from retail.models import Product,ProductCatogory 
from retail.models import Product



class AddProductSerializer(serializers.Serializer):

    category = serializers.PrimaryKeyRelatedField(queryset=ProductCatogory.objects.all())
    name = serializers.CharField()
    product_pic = serializers.FileField()
    price = serializers.CharField()
    desc = serializers.CharField()
 
    def validate(self, attrs):
            
            user = self.context['user']
            name=attrs.get('name')
            category=attrs.get('category')
            price=attrs.get('price')
            desc=attrs.get('desc')
    
            if Product.objects.filter(user=user,name=name,category=category,price=price,desc=desc).exists():
                raise serializers.ValidationError('You have already added this product.')
            
            return attrs 

    def create(self, validated_data):
        user = self.context['user']
        product = Product.objects.create(
            category=validated_data['category'],
            name=validated_data['name'],
            product_pic=validated_data['product_pic'],
            price=validated_data['price'],
            desc=validated_data['desc'],
            user=user)
        
        return product
    

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
    