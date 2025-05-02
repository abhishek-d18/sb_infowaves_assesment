from django.db import models

class Restaurants(models.Model):
    name = models.CharField(max_length= 255, null=True, blank=True)
    location = models.CharField(max_length= 255)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    name = models.CharField(max_length= 255)
    restaurant_id = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits= 10, decimal_places= 2, null=True, blank=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    dish_id = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length= 255)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length= 20, choices= STATUS_CHOICES, default='Pending')



    