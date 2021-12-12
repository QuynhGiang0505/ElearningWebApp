from django import urls
from django.contrib import admin
from django.urls import path,include
from GTEAMS_APP import views
from django.conf.urls import url, handler404, handler500
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('GTEAMS/', include("GTEAMS_APP.urls")),
    path('accounts/',include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path('tinymce/',include('tinymce.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
