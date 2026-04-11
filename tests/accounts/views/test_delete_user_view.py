from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

class TestDeleteUserView(TestCase):
    def setUp(self):
        self.user_credentials = {
            'email': 'test@test.com',
            'username': 'TestUser',
            'password': '12test34'
        }
        self.user = UserModel.objects.create_user(**self.user_credentials)
        self.client.login(
            email=self.user_credentials['email'],
            password=self.user_credentials['password']
        )

    def test__user_can_delete_own_account(self):
        response = self.client.post(
            reverse('delete-profile', kwargs={'pk': self.user.pk})
        )

        self.assertRedirects(response, reverse('home-page'))
        self.assertFalse(UserModel.objects.filter(pk=self.user.pk).exists())