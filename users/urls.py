from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_api_view, name='register'),
    path('authorization/', views.authorization_api_view, name='login'),
    path('confirm/', views.confirmation_api_view, name='confirm'),
]