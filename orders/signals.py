from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from orders.tasks import _send_order_confirmation_email


@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if created:
        if settings.DEBUG:
            _send_order_confirmation_email.delay(
                subject="Order confirmation",
                message=f"Hi {instance.user.username}, your order #{instance.id} has been placed successfully.",
                from_email=settings.DEFAULT_EMAIL,
                recipient_list=[instance.user.email],
            )
        else:
            _send_order_confirmation_email(
                subject="Order confirmation",
                message=f"Hi {instance.user.username}, your order #{instance.id} has been placed successfully.",
                from_email=settings.COMPANY_EMAIL_EMAIL,
                recipient_list=[instance.user.email],
            )