from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='log'),
    path('register/', views.registerPage, name='reg'),
    path('logout/', views.logoutUser,name='logout')
]

