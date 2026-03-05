from django.db import models

class Product(models.Model):
    image = models.ImageField(
        upload_to="media/",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    price = models.TextField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
