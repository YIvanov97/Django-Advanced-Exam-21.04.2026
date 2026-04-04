from django.urls import path
from orders.api import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='api-orders'),
]