from django.urls import path, include
from cart import views
urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('<slug:product_slug>/', include([
        path('add/', views.AddToCartView.as_view(), name='add-to-cart'),
        path('remove/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    ])),
    path('remove-all/', views.RemoveAllFromCartView.as_view(), name='remove-all-from-cart'),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
]