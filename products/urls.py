from django.urls import path, include
from products import views

urlpatterns = [
    path('catalog/', views.Catalog.as_view(), name='catalog'),
    path('add/', views.AddProduct.as_view(), name='add-product'),
    path('product/<slug:product_slug>/', include([
        path('', views.ProductDetail.as_view(), name='product-details'),
    ])),
]
