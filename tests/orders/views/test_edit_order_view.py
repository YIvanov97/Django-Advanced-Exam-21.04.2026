from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from orders.models import Order
from orders.choices.status_choices import StatusChoices

UserModel = get_user_model()


class TestOrderViews(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='user@test.com',
            username='TestUser',
            password='12test34',
        )
        self.other_user = UserModel.objects.create_user(
            email='other@test.com',
            username='OtherUser',
            password='12test34',
        )
        self.staff_user = UserModel.objects.create_user(
            email='staff@test.com',
            username='StaffUser',
            password='12test34',
            is_staff=True,
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

    def test__owner_can_edit_pending_order(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('order-edit', kwargs={'pk': self.order.pk}),
            data={
                'first_name': 'Testedit',
                'last_name': 'Testovedit',
                'address': 'Address edit',
                'city': 'Sofia edit',
                'phone_number': '0999 999 999',
            }
        )

        self.order.refresh_from_db()
        self.assertRedirects(response, reverse('order-details', kwargs={'pk': self.order.pk}))
        self.assertEqual(self.order.first_name, 'Testedit')
        self.assertEqual(self.order.city, 'Sofia edit')

    def test__staff_can_update_order_status(self):
        self.client.force_login(self.staff_user)

        response = self.client.post(
            reverse('order-status-update', kwargs={'pk': self.order.pk}),
            data={'status': StatusChoices.DELIVERED}
        )

        self.order.refresh_from_db()
        self.assertRedirects(response, reverse('order-details', kwargs={'pk': self.order.pk}))
        self.assertEqual(self.order.status, StatusChoices.DELIVERED)

    def test__non_owner_cannot_view_order_details(self):
        self.client.force_login(self.other_user)

        response = self.client.get(
            reverse('order-details', kwargs={'pk': self.order.pk})
        )

        self.assertEqual(response.status_code, 403)

    def test__non_owner_cannot_edit_pending_order(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse('order-edit', kwargs={'pk': self.order.pk}),
            data={
                'first_name': 'Testedit',
                'last_name': 'Testovedit',
                'address': 'Address edit',
                'city': 'Sofia edit',
                'phone_number': '0999 999 999',
            }
        )

        self.order.refresh_from_db()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.order.first_name, 'Test')