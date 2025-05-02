from django.shortcuts import render
from .serializers import RestaurantSerializer, DishSerializer, OrderSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Restaurants, Dishes, Orders

class RestaurantListCreateView(ListCreateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer

class DishesListCreateView(ListCreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishSerializer

class OrdersListCreateView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrdersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
