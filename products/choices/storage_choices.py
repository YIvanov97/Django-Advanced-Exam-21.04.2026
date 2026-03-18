from django.db import models

class StorageChoices(models.IntegerChoices):
    STORAGE_128 = 128, "128 GB"
    STORAGE_256 = 256, "256 GB"
    STORAGE_512 = 512, "512 GB"
    STORAGE_1TB = 1, "1 TB"
    STORAGE_2TB = 2, "2 TB"
    STORAGE_4TB = 3, "4 TB"