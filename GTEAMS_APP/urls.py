from django.conf import urls
from django.urls import path, include
from GTEAMS_APP.models import *
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from GTEAMS_APP.models import Practice


urlpatterns = [
    # path('', views.PageHome, name='home'),
    path('', views.showCoursesMainPage, name='home'),
    path('<str:title>', views.show_detail_MainPage, name='show_detail_MainPage'),
    path('intro/',views.PageIntro,name="intro"),
    path('contact/', views.create_contact, name='contact'),

    path('courses/', views.showCourses, name='courses'),
    path('courses/<str:title>', views.seeCourse, name='seeCourse'),
    path('courses/<subject>', views.showcourses_detail_demo, name='coursesVideo'),
    path('courses/<subject>/<title>', views.showcourses_detail_demo),
    path('<str:title>', views.show_detail_course, name='123'),
    path('courses/addCart/', views.addCart, name="buy"),
    path('courses/cart/', views.cartShopping, name="shopping"),
    path('courses/detailCart/', views.detailCart, name="detailCart"),

    path('blog/', views.blogHome, name='blogs'),
    path('blog/<str:slug>', views.blogPost, name='blogspost'),
    path('login/', views.PageLogin,name='login'),
    path('register/', views.PageRegister,name='register'),
    path('practice/',views.ShowQuestions, name='practice'),
    path('practice/<title>/',views.ShowQuestionsID, name='practiceID'),
    path('error/',views.error, name='error')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

