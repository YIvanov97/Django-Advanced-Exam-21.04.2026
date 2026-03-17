from django.db import models

class ScreenSizeChoices(models.IntegerChoices):
    SIZE_13 = 13, "13 inch"
    SIZE_14 = 14, "14 inch"
    SIZE_15 = 15, "15.6 inch"
    SIZE_16 = 16, "16 inch"
    SIZE_17 = 17, "17.3 inch"