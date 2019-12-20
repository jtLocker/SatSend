from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_request, name = 'login'),
    path('logout', views.logout_request, name = 'logout')
]