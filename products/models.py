from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from products.choices.category_choices import CategoryChoices
from products.choices.ram_choices import RamChoices
from products.choices.screen_size_choices import ScreenSizeChoices
from products.choices.storage_choices import StorageChoices
from common.validators import InputFieldValidator, DigitFieldValidator
from django.utils.text import slugify

UserModel = get_user_model()

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            InputFieldValidator(message="Product name contains invalid characters.")
        ]
    )
    description = models.CharField(
        max_length=3000,
        validators=[
            InputFieldValidator(message="Product description contains invalid characters.")
        ]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices
    )
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating and not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")
            super().save(update_fields=['slug'])

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = CloudinaryField(
        "image",
        folder="products",
    )

class Laptop(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="laptop",
    )
    processor = models.CharField(
        max_length=100,
        validators=[
            InputFieldValidator(message="Processor contains invalid characters.")
        ]
    )
    ram = models.PositiveIntegerField(
        choices=RamChoices,
    )
    storage = models.PositiveIntegerField(
        choices=StorageChoices,
    )
    screen_size = models.PositiveIntegerField(
        choices=ScreenSizeChoices,
    )
    gpu = models.CharField(
        max_length=100,
        validators=[
            InputFieldValidator(message="GPU contains invalid characters.")
        ]
    )

class Computer(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="computer",
    )
    processor = models.CharField(
        max_length=100,
        validators=[
            InputFieldValidator(message="Processor contains invalid characters.")
        ]
    )
    ram = models.PositiveIntegerField(
        choices=RamChoices,
    )
    storage = models.PositiveIntegerField(
        choices=StorageChoices,
    )
    gpu = models.CharField(
        max_length=100,
        validators=[
            InputFieldValidator(message="GPU contains invalid characters.")
        ]
    )

class Keyboard(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="keyboard",
    )
    switch_type = models.CharField(
        max_length=50,
        validators=[
            InputFieldValidator(message="Switch type contains invalid characters.")
        ]
    )
    keyboard_layout = models.CharField(
        max_length=50,
        validators=[
            InputFieldValidator(message="Keyboard layout contains invalid characters.")
        ]
    )
    rgb_lighting = models.BooleanField(default=False)
    wireless = models.BooleanField(default=False)

class Mouse(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="mouse",
    )
    dpi = models.PositiveIntegerField()
    wireless = models.BooleanField(default=False)

class Headphones(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="headphones",
    )
    wireless = models.BooleanField(default=False)
    noise_cancelling = models.BooleanField(default=False)
    battery_life = models.CharField(
        max_length=50,
        blank=True,
        validators=[
            DigitFieldValidator()
        ]
    )
    microphone = models.BooleanField(default=False)

class Speakers(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="speakers",
    )
    power_output = models.PositiveIntegerField()
    bluetooth = models.BooleanField(default=False)
    portable = models.BooleanField(default=False)

class Review(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
