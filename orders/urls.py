from django.urls import path, include

from orders import views

urlpatterns = [
    path("", views.OrderListView.as_view(), name="orders"),
    path("<int:pk>/", include([
        path('', views.OrderDetailView.as_view(), name='order-details'),
        path('update/', views.OrderStatusUpdateView.as_view(), name='order-status-update'),
    ])),
]