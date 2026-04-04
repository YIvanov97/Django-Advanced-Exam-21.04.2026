from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from accounts.models import Profile

UserModel = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter your email"}),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
        label="Password"
    )

    error_messages = {
        "invalid_login": "Invalid email or password."
    }

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username', 'email')
        help_texts = {}
        error_messages = {
            "username": {
                "required": "Please enter username.",
                "unique": "This username is already taken.",
            },
            "email": {
                "required": "Please enter email.",
                "unique": "This email is already registered.",
            },
        }

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Enter last name"}
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "class": 'form-control',
                    "type": "date",
                    "placeholder": "Enter date of birth"
                }
            ),
        }

class ProfileEditForm(ProfileBaseForm):
    pass

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email']

class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth']