from django import urls
from django.urls import path
from django.conf.urls import url, include

from . import views
from .views import activate  

urlpatterns = [
    path('login/', views.loginPage, name='log'),
    path('register/', views.registerPage, name='reg'),
    path('logout/', views.logoutUser,name='logout'),
    url(r'auth-social/', include('social_django.urls', namespace='social')),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]


