from django.core.exceptions import ValidationError
from django.test import TestCase

from products.models import Product
from products.choices.category_choices import CategoryChoices


class TestProductModel(TestCase):
    def test__product_with_negative_price__raises_validation_error(self):
        product = Product(
            name='Test',
            description='description',
            price=-5,
            category=CategoryChoices.LAPTOP,
        )

        with self.assertRaises(ValidationError):
            product.full_clean()

    def test__product_with_invalid_name_characters__raises_validation_error(self):
        product = Product(
            name='@@@',
            description='description',
            price=100,
            category=CategoryChoices.LAPTOP,
        )

        with self.assertRaises(ValidationError):
            product.full_clean()