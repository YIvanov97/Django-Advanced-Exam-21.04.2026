from django.urls import path, include
from common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
]