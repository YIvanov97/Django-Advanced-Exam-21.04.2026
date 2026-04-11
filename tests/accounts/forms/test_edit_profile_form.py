from django.test import TestCase
from accounts.forms import ProfileEditForm

class TestProfileEditForm(TestCase):
    def test__profile_form_with_invalid_first_name__characters_is_invalid(self):
        form = ProfileEditForm(data={
            'first_name': '@@@',
            'last_name': 'Test',
            'date_of_birth': '2000-01-01',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(
            'First name contains invalid characters.',
            form.errors['first_name'][0]
        )

    def test__profile_form_with_invalid_last_name__characters_is_invalid(self):
        form = ProfileEditForm(data={
            'first_name': 'Test',
            'last_name': '@@@',
            'date_of_birth': '2000-01-01',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(
            'Last name contains invalid characters.',
            form.errors['last_name'][0]
        )