from django.db import models

class StatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    PROCESSING = "processing", "Processing"
    DELIVERED = "delivered", "Delivered"