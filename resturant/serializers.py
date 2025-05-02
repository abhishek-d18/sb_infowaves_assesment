from .models import Restaurants, Dishes, Orders
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'