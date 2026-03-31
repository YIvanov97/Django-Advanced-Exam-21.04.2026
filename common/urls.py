from django.urls import path, include
from common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('about/', views.AboutPageView.as_view(), name='about-page'),
    path("contact/", views.ContactPageView.as_view(), name="contact-page"),
]