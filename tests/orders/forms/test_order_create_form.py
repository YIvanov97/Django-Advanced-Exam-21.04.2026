from django.test import TestCase
from orders.forms import OrderCreateForm


class TestOrderCreateForm(TestCase):
    def test__order_create_form_with_valid_data__is_valid(self):
        form = OrderCreateForm(data={
            'first_name': 'Test',
            'last_name': 'Testov',
            'address': 'Address',
            'city': 'Sofia',
            'phone_number': '0888 888 888',
        })

        self.assertTrue(form.is_valid())

    def test__order_create_form_without_first_name__returns_custom_error(self):
        form = OrderCreateForm(data={
            'first_name': '',
            'last_name': 'Testov',
            'address': 'Address',
            'city': 'Sofia',
            'phone_number': '0888 888 888',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual('Please enter your first name.', form.errors['first_name'][0])