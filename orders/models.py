from django.contrib.auth import get_user_model
from django.db import models

from orders.choices.status_choices import StatusChoices
from products.models import Product

UserModel = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(Product, through="OrderItem", related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.PENDING)
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20
    )
    address = models.CharField(
        max_length=200
    )
    city = models.CharField(
        max_length=50
    )
    phone_number = models.CharField(
        max_length=20
    )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
