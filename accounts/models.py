from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from accounts.managers import AppUserManager
from common.validators import InputFieldValidator


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            MinLengthValidator(4, message="Username must be at least 4 characters long."),
            InputFieldValidator(message="Username contains invalid characters.")
        ],
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            InputFieldValidator(message="First name contains invalid characters.")
        ],
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            InputFieldValidator(message="Last name contains invalid characters.")
        ],
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )