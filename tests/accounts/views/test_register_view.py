from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from accounts.models import Profile

UserModel = get_user_model()


class TestRegisterView(TestCase):
    def test__register_valid_user_redirects_to_login_and_creates_profile(self):
        response = self.client.post(reverse('register'), data={
            'email': 'test@test.com',
            'username': 'TestUser',
            'password1': '12test34',
            'password2': '12test34',
        })

        self.assertRedirects(response, reverse('login'))
        self.assertTrue(UserModel.objects.filter(email='test@test.com').exists())

        user = UserModel.objects.get(email='test@test.com')
        self.assertTrue(Profile.objects.filter(pk=user.pk).exists())