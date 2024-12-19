from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Product, CartItems



#Using model serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'username', 'passowrd']
        extra = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source = '')
    product_prize = serializers.ReadOnlyField(source = '')

    class Meta:
        model = CartItems
        fields = ['id', 'user', 'product', 'quatity', 'product_name', 'product_price']
    

    



