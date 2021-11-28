from django.contrib import admin
from GTEAMS_APP.models import *
from  django.contrib.admin.widgets import AdminTextareaWidget
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","title","content")
    search_fields= ("name","TieuDe")
    list_filter = ("name","email")
class AnswerInline(admin.TabularInline):
    model=Answer
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]
admin.site.register(Quiz)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Contact)

admin.site.register(Courses)
admin.site.register(subjects)
admin.site.register(typeCourse)
admin.site.register(Post)
admin.site.register(article_quiz)
admin.site.register(article_blog)

