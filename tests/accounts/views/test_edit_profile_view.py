from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

class TestEditProfileView(TestCase):
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

    def test__owner_can_edit_own_profile(self):
        response = self.client.post(
            reverse('edit-profile', kwargs={'pk': self.user.pk}),
            data={
                'first_name': 'Test',
                'last_name': 'Testov',
                'date_of_birth': '2000-01-01',
            }
        )
        self.assertRedirects(response, reverse('profile-details', kwargs={'pk': self.user.pk}))
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.first_name, 'Test')