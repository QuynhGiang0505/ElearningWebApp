from django.conf import urls
from django.urls import path, include
from GTEAMS_APP.models import *
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from GTEAMS_APP.models import Practice
app_name='gteam'

urlpatterns = [
    path('', views.PageHome, name='home'),
    path('contact/', views.create_contact, name='contact'),
    path('courses/', views.showCourses, name='courses'),
   
    path('courses/<subject>', views.showcourses_detail_demo, name='coursesVideo'),
    path('courses/<subject>/<title>', views.showcourses_detail_demo),

    path('<str:title>', views.show_detail_course, name='123'),

    path('blog/', views.PageBlogs, name='blogs'),
    path('login/', views.PageLogin,name='login'),
    path('register/', views.PageRegister,name='register'),
    path('practice/',views.ShowQuestions, name='practice'),
    path('practice/<title>/',views.ShowQuestionsID, name='practiceID'),
    path('error/',views.error, name='error')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

