from django.db import models

class RamChoices(models.IntegerChoices):
    RAM_4 = 4, "4 GB"
    RAM_8 = 8, "8 GB"
    RAM_16 = 16, "16 GB"
    RAM_32 = 32, "32 GB"
    RAM_64 = 64, "64 GB"