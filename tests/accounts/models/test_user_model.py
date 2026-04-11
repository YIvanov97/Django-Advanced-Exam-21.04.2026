from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import Profile

UserModel = get_user_model()


class TestAppUserModel(TestCase):
    def test__create_user_profile(self):
        user = UserModel.objects.create_user(
            email='test@test.com',
            username='TestUser',
            password='12test34'
        )
        self.assertTrue(Profile.objects.filter(pk=user.pk).exists())

    def test__username_with_less_than_four_characters__raises_validation_error(self):
        user = UserModel(
            email='test@test.com',
            username='abc',
            password='12test34'
        )

        with self.assertRaises(ValidationError):
            user.full_clean()