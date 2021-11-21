from django import urls
from django.contrib import admin
from django.urls import path,include
from GTEAMS_APP import views
from django.conf.urls import url, handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("GTEAMS_APP.urls")),
    path('accounts/',include("accounts.urls"))
]
handler404 = 'GTEAMS_APP.views.error'