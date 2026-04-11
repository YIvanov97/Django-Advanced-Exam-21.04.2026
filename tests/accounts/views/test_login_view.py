from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestLoginView(TestCase):
    def setUp(self):
        self.user_credentials = {
            'email': 'test@test.com',
            'username': 'TestUser',
            'password': '12test34',
        }
        self.user = UserModel.objects.create_user(**self.user_credentials)

    def test__login_with_invalid_credentials__shows_error(self):
        response = self.client.post(reverse('login'), data={
            'username': 'test@test.com',
            'password': '12test56',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid email or password.')

    def test__login_with_valid_credentials__redirects_successfully(self):
        response = self.client.post(reverse('login'), data={
            'username': 'test@test.com',
            'password': '12test34',
        })

        self.assertEqual(response.status_code, 302)