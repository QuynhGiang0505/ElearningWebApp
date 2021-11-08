

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url


from GTEAMS_APP.models import Practice
app_name='gteam'
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.PageContact, name='contact'),
    path('courses/', views.showCourses, name='courses'),
   
    path('courses/<subject>', views.showcourses_detail_demo, name='coursesVideo'),
    path('courses/<subject>/<title>', views.showcourses_detail_demo),

     path('<str:title>', views.show_detail_course, name='123'),

    path('blog/', views.PageBlogs, name='blogs'),
    path('login/', views.PageLogin, name='login'),
    path('register/', views.PageRegister, name='register'),
    path('NewContact/', views.create_contact, name='NewContact'),
    path('Practice/',views.ShowQuestions, name='practice'),
    path('Practice/<title>',views.ShowQuestionsID, name='practiceID'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)