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
        fields = '__all__'

class ProfileEditForm(ProfileBaseForm):
    pass