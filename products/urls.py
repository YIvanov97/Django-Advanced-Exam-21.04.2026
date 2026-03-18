from django.urls import path, include
from products import views

urlpatterns = [
    path('catalog/', views.Catalog.as_view(), name='catalog'),
    path('add/', views.AddProductView.as_view(), name='add-product'),
    path('product/<slug:product_slug>/', include([
        path('', views.ProductDetailView.as_view(), name='product-details'),
        path('edit/', views.ProductEditView.as_view(), name='product-edit'),
        path('delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    ])),
]
