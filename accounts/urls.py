from django.contrib.auth.views import LoginView, LogoutView

from accounts import views
from django.urls import path, include

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("profile/<int:pk>/", include([
        path("", views.ProfileView.as_view(), name="profile-details"),
        path("edit/", views.ProfileEditView.as_view(), name="edit-profile"),
        # path("delete/", views.profile_delete_view, name="profile-delete"),
    ]))
]