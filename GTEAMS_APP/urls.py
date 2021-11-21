from django.conf import urls
from django.urls import path
from django.conf.urls import url

from GTEAMS_APP.models import Practice

from . import views
urlpatterns = [
    path('', views.PageHome),
    path('contact/', views.create_contact, name='NewContact'),
    path('blog/', views.PageBlog),
    path('Practice/',views.ShowQuestions, name='practice'),
    path('Practice/<title>',views.ShowQuestionsID, name='practiceID')
]