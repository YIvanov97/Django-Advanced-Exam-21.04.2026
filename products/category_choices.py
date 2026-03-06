from django.db import models

class CategoryChoices(models.TextChoices):
    LAPTOP = 'laptop', 'Laptop'
    COMPUTER = 'computer', 'Computer'
    KEYBOARD = 'keyboard', 'Keyboard'
    MOUSE = 'mouse', 'Mouse'
    HEADPHONES = 'headphones', 'Headphones'
    SPEAKERS = 'speakers', 'Speaker'
    OTHER = 'other', 'Other'