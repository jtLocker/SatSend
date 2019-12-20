from django.urls import path, include
from . import views

urlpatterns = [
    path('address', views.address, name='address'),
]