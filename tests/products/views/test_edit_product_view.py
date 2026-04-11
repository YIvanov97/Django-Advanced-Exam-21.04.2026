from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.models import Product, Laptop
from products.choices.category_choices import CategoryChoices

UserModel = get_user_model()


class TestEditProductView(TestCase):
    def setUp(self):
        self.staff_user = UserModel.objects.create_user(
            email='staff@test.com',
            username='Staff',
            password='12test34',
            is_staff=True,
        )
        self.normal_user = UserModel.objects.create_user(
            email='test@test.com',
            username='TestUser',
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
            processor='Intel i5',
            ram=8,
            storage=256,
            screen_size=15,
            gpu='RTX 3050',
        )

    def test__staff_can_edit_product(self):
        self.client.force_login(self.staff_user)

        response = self.client.post(
            reverse('product-edit', kwargs={'product_slug': self.product.slug}),
            data={
                'name': 'Test edit',
                'description': 'description edit',
                'price': '200',
                'category': CategoryChoices.LAPTOP,
                'laptop-processor': 'Intel i7',
                'laptop-ram': 16,
                'laptop-storage': 512,
                'laptop-screen_size': 17,
                'laptop-gpu': 'RTX 4060',
            }
        )

        self.product.refresh_from_db()
        self.product.laptop.refresh_from_db()
        self.assertRedirects(response, reverse('product-details', kwargs={'product_slug': self.product.slug}))
        self.assertEqual(self.product.name, 'Test edit')
        self.assertEqual(self.product.description, 'description edit')
        self.assertEqual(self.product.price, 200)
        self.assertEqual(self.product.laptop.processor, 'Intel i7')
        self.assertEqual(self.product.laptop.ram, 16)

    def test__non_staff_cannot_edit_product(self):
        self.client.force_login(self.normal_user)

        response = self.client.post(
            reverse('product-edit', kwargs={'product_slug': self.product.slug}),
            data={
                'name': 'Test edit',
                'description': 'description edit',
                'price': '200',
                'category': CategoryChoices.LAPTOP,
                'laptop-processor': 'Intel i7',
                'laptop-ram': 16,
                'laptop-storage': 512,
                'laptop-screen_size': 17,
                'laptop-gpu': 'RTX 4060',
            }
        )

        self.product.refresh_from_db()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.product.name, 'Test')