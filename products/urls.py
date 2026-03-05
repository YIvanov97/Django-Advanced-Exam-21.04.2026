from django.urls import path, include
from products import views

urlpatterns = [
    path('catalog/', views.Catalog.as_view(), name='catalog'),
    path('product/', include([
        path('add/', views.AddProduct.as_view(), name='add-product'),
        # path('approve/<int:pk>/', views.approve_post, name='approve_post'),
        # path('edit/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
        # path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
        # path('details/<int:pk>/', views.PostDetails.as_view(), name='post_details'),
    ])),
    # path('redirect/', views.MyRedirectView.as_view(), name='redirect'),
]
