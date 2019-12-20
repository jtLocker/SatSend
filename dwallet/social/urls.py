from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.friend_req, name='friend_req'),
]