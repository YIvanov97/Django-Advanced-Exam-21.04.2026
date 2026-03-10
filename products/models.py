from django.db import models

from products.category_choices import CategoryChoices


class Product(models.Model):
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    price = models.TextField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        choices=CategoryChoices,
        default=CategoryChoices.OTHER,
        max_length=50
    )

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
