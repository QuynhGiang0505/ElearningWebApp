from django.contrib import admin
from GTEAMS_APP.models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","title","content")
    search_fields= ("name","TieuDe")
    list_filter = ("name","email")

admin.site.register(Practice)
admin.site.register(Practice_title)
admin.site.register(Contact)

admin.site.register(Courses)
admin.site.register(subjects)
admin.site.register(typeCourse)
admin.site.register(Post)
