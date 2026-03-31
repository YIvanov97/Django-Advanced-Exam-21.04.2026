from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

UserModel = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=1)