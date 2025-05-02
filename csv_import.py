from resturant.models import Restaurant, Dishes, Orders
import csv
from django.db import transaction

def import_orders_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['DishName', 'RestaurantName', 'CustomerName'])

        for row in reader:
            dish_name = row['DishName'].strip()
            restaurant_name = row['RestaurantName'].strip()
            customer_name = row['CustomerName'].strip()
            
            try:
                resturant = Restaurant.objects.get(name=restaurant_name)
                dish = Dishes.objects.get(name=dish_name, restaurant_id=resturant)
                order = Orders(dish_id=dish, customer_name=customer_name)
                
                Orders.objects.create(dish = dish, customer_name=customer_name)
                print(f"Order created for {customer_name} with dish {dish_name} from restaurant {restaurant_name}.")

            except Restaurant.DoesNotExist:
                print(f"Restaurant '{restaurant_name}' does not exist. Skipping order for {customer_name}.")
            except Dishes.DoesNotExist:
                print(f"Dish '{dish_name}' does not exist in restaurant '{restaurant_name}'. Skipping order for {customer_name}.")
            except Exception as e:
                print(f"An error occurred while creating order for {customer_name}: {e}")



