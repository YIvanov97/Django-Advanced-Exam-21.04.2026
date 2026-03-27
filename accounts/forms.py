from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Profile

UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username', 'email')
        help_texts = {}

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