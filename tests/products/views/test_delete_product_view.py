from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.models import Product, Laptop
from products.choices.category_choices import CategoryChoices

UserModel = get_user_model()


class TestDeleteProductView(TestCase):
    def setUp(self):
        self.staff_user = UserModel.objects.create_user(
            email='staff@test.com',
            username='Staff',
            password='12test34',
            is_staff=True,
        )
        self.normal_user = UserModel.objects.create_user(
            email='user@test.com',
            username='NormalUser',
            password='12test34',
        )

        self.product = Product.objects.create(
            name='Test',
            description='description',
            price=100,
            category=CategoryChoices.LAPTOP,
        )

        self.laptop = Laptop.objects.create(
            product=self.product,
            processor='Intel i7',
            ram=8,
            storage=256,
            screen_size=15,
            gpu='RTX 3050',
        )

    def test__staff_can_delete_product(self):
        self.client.force_login(self.staff_user)

        response = self.client.post(
            reverse('product-delete', kwargs={'product_slug': self.product.slug})
        )

        self.assertRedirects(response, reverse('catalog'))
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

    def test__non_staff_cannot_delete_product(self):
        self.client.force_login(self.normal_user)

        response = self.client.post(
            reverse('product-delete', kwargs={'product_slug': self.product.slug})
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Product.objects.filter(pk=self.product.pk).exists())