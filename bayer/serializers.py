from rest_framework import serializers

class CartProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    product_pic = serializers.ImageField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)