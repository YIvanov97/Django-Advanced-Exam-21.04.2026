from django.contrib.auth import get_user_model
from django.test import TestCase

from orders.models import Order, OrderItem
from orders.choices.status_choices import StatusChoices
from products.models import Product
from products.choices.category_choices import CategoryChoices

UserModel = get_user_model()


class TestOrderModel(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            username='TestUser',
            password='12test34',
        )
        self.product = Product(
            name='Test',
            description='description',
            price=100,
            category=CategoryChoices.LAPTOP,
        )
        self.product.save()

    def test__order_is_created_with_pending_status(self):
        order = Order.objects.create(
            user=self.user,
            total_price=100,
            status=StatusChoices.PENDING,
            first_name='Test',
            last_name='Testov',
            address='Address',
            city='Sofia',
            phone_number='0888 888 888',
        )

        self.assertEqual(order.user, self.user)
        self.assertEqual(order.status, StatusChoices.PENDING)
        self.assertEqual(order.total_price, 100)

    def test__deleting_order_deletes_related_order_item(self):
        order = Order.objects.create(
            user=self.user,
            total_price=100,
            status=StatusChoices.PENDING,
            first_name='Test',
            last_name='Testov',
            address='Address',
            city='Sofia',
            phone_number='0888 888 888',
        )

        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=1,
            price=100,
        )

        order.delete()
        self.assertFalse(OrderItem.objects.filter(pk=order_item.pk).exists())