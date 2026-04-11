from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from orders.models import Order
from orders.choices.status_choices import StatusChoices

UserModel = get_user_model()


class TestDeleteOrderView(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='user@test.com',
            username='TestUser',
            password='12test34',
        )

        self.order = Order.objects.create(
            user=self.user,
            total_price=100,
            status=StatusChoices.PENDING,
            first_name='Test',
            last_name='Testov',
            address='Address',
            city='Sofia',
            phone_number='0888 888 888',
        )

    def test__owner_can_delete_pending_order(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('order-delete', kwargs={'pk': self.order.pk})
        )

        self.assertRedirects(response, reverse('orders'))
        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())