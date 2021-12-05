from django.conf import urls
from django.urls import path, include
from GTEAMS_APP.models import *
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url




urlpatterns = [
    # path('', views.PageHome, name='home'),
    path('', views.showCoursesMainPage, name='home'),
    path('<str:title>', views.show_detail_MainPage, name='show_detail_MainPage'),
    path('intro/',views.PageIntro,name="intro"),
    path('contact/', views.create_contact, name='contact'),
    path('practice/',views.ShowListQuiz, name='practice'),
    path('courses/', views.showCourses, name='courses'),
    path('courses/yourCart/', views.cartShopping, name="shopping"),
    path('courses/addCart/', views.addCart, name="buy"),
    path('courses/detailCart/', views.detailCart, name="detailCart"),
    path('blog/', views.blogHome, name='blogs'),
    path('quiz/', views.quizHome, name='quizs'),
    path('login/', views.PageLogin,name='login'),
    path('error/',views.error, name='error'),
    path('searchblog/', views.search_blog, name="searchblog"),
    path('searchquiz/', views.search_quiz, name="searchquiz"),
    path('register/', views.PageRegister,name='register'),
    path('profile/',views.PageProfilee, name='profile'),
    path('courses/<title>/', views.seeCourse, name='seeCourse'),
    path('courses/subject/<subject>/', views.showcourses_detail_demo, name='coursesVideo'),
    path('<str:title>/', views.show_detail_course, name='123'),
    path('courses/cart/delete/<id>/', views.delItem, name="del"),
    path('blog/<str:slug>', views.blogPost, name='blogspost'),
    path('quiz/<str:slug>', views.quizPost, name='quizspost'),
    path('practice/<topic>/',views.ShowQuiz, name='practiceID'),
    path('practice/<topic>/data/',views.ShowQuizID, name='QuizID'),
    path('practice/<topic>/save/',views.save_quiz_view, name='QuizSave'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

