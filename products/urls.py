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
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
    path('review/<int:pk>/edit/', views.ReviewEditView.as_view(), name='review-edit'),
    path("favorites/", views.FavoriteProductsView.as_view(), name="favorites"),
    path("favorites/<int:pk>/toggle/", views.ToggleFavoriteView.as_view(), name="toggle-favorite"),
]
