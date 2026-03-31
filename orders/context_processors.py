from orders.choices.status_choices import StatusChoices
from orders.models import Order

def pending_orders_count(request):
    return {
        "pending_orders_count": Order.objects.filter(status=StatusChoices.PENDING).count()
    }