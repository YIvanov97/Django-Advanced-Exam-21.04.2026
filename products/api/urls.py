from django.urls import path

from products.api import views

urlpatterns = [
    path('catalog/', views.Catalog.as_view(), name='api-catalog'),
]