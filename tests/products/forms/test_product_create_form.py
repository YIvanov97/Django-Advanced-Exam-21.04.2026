from django.test import TestCase

from products.forms import ProductCreateForm
from products.choices.category_choices import CategoryChoices


class TestProductForms(TestCase):
    def test__product_create_form_with_valid_data__is_valid(self):
        form = ProductCreateForm(data={
            'name': 'Test',
            'description': 'description',
            'price': '1500',
            'category': CategoryChoices.LAPTOP,
        })

        self.assertTrue(form.is_valid())

    def test__product_create_form_without_name__returns_custom_error(self):
        form = ProductCreateForm(data={
            'name': '',
            'description': 'description',
            'price': '1500',
            'category': CategoryChoices.LAPTOP,
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(
            'Please enter the product name.',
            form.errors['name'][0]
        )