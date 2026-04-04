from django.urls import path, include

from orders import views

urlpatterns = [
    path('checkout/', views.OrderCreateView.as_view(), name='checkout'),
    path("", views.OrderListView.as_view(), name="orders"),
    path("<int:pk>/", include([
        path('', views.OrderDetailView.as_view(), name='order-details'),
        path('edit/', views.OrderEditView.as_view(), name='order-edit'),
        path('delete/', views.OrderDeleteView.as_view(), name='order-delete'),
        path('update/', views.OrderStatusUpdateView.as_view(), name='order-status-update'),
    ])),
]