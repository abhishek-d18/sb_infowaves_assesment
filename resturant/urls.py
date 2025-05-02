from django.urls import path, include
from .views import RestaurantListCreateView, DishesListCreateView, OrdersListCreateView, OrdersRetrieveUpdateDestroyView

urlpatterns = [
    path('resturants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    # path('resturants/<int:pk>/', RestaurantListCreateView.as_view(), name='restaurant-detail'),
    # path('resturants/<int:pk>/update/', RestaurantListCreateView.as_view(), name='restaurant-update'),

    path('dishes/', DishesListCreateView.as_view(), name='dishes-list-create'),
    # path('dishes/<int:pk>/', DishesListCreateView.as_view(), name='dishes-detail'),
    # path('dishes/<int:pk>/update/', DishesListCreateView.as_view(), name='dishes-update'),

    path('orders/', OrdersListCreateView.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', OrdersRetrieveUpdateDestroyView.as_view(), name='orders-detail'),

]
