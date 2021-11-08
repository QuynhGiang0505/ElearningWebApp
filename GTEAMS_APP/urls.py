from django.conf import urls
from django.urls import path
from django.conf.urls import url
from GTEAMS_APP.models import *
from django.conf.urls import url

from . import views
urlpatterns = [
    path('', views.PageHome, name='home'),
    path('contact/', views.create_contact, name='contact'),
    path('blog/', views.PageBlog, name='blog'),
    path('login/', views.PageLogin,name='login'),
    path('register/', views.PageRegister,name='register'),
    path('practice/',views.ShowQuestions, name='practice'),
    path('practice/<title>/',views.ShowQuestionsID, name='practiceID'),
    path('error/',views.error, name='error')
]
