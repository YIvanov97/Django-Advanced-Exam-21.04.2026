from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.forms import RegisterForm

UserModel = get_user_model()


class TestRegisterForm(TestCase):
    def test__register_form_with_duplicate_email_is_invalid(self):
        UserModel.objects.create_user(
            email='test@test.com',
            username='TestUser',
            password='12test34'
        )

        form = RegisterForm(data={
            'email': 'test@test.com',
            'username': 'NewUser',
            'password1': '12test34',
            'password2': '12test34',
        })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['email'])

    def test__register_form_with_valid_data_is_valid(self):
        form = RegisterForm(data={
            'email': 'test@test.com',
            'username': 'TestUser',
            'password1': '12test34',
            'password2': '12test34',
        })

        self.assertTrue(form.is_valid())