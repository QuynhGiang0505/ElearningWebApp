from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
import datetime
from django.http import HttpResponse

import GTEAMS_APP
from GTEAMS_APP.models import *
from GTEAMS_APP.form import *
from django.contrib.auth.decorators import login_required

def PageContact(request):
    return render(request,'pages/contact.html')
def PagePractice(request):
    return render(request,'pages/practice.html')
def PageBlogs(request):
    return render(request,'pages/blogs.html')
def PageIntro(request):
    return render(request,'pages/intro.html')
@login_required(login_url='../../accounts/login')

def PageLogin(request):
    return render(request,'pages/login.html')
def PageRegister(request):
    return render(request,'pages/register.html')
def PageCourses(request):
    return render(request,'pages/courses.html')

# HOME
def showCoursesMainPage(request):
    allCourses=Courses.objects.all()
    latest_post = Courses.objects.order_by('-date')[:4]
    return render(request,'pages/HomePage.html',{'allCourses': allCourses})

def show_detail_MainPage(request,title):
    try:
        Content=Courses.objects.filter(title=title)
    except Courses.DoesNotExist:
        raise Http404("Practice doesnot exist")
    a=Courses.objects.all()
    context= {'title':title,'question':Content,'a':a}
    return render(request,'pages/coursesVideo.html',context)
#-------------------------------------------------------------------------


def create_contact(request):
    if request.method == 'GET':
        form=CreateNewContact()
    if request.method == 'POST':
        form=CreateNewContact(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'pages/contact.html',{'form':form})
def ShowQuestions(request):
    Question=Practice_title.objects.all()
    context = {'question': Question}
    return render(request,'pages/practice.html',context)

def ShowQuestionsID(request,title):
    try:
        Content=Practice.objects.filter(title=title)
    except Practice.DoesNotExist:
        raise Http404("Practice doesnot exist")
    
    context= {'title':title,'question':Content}
    return render(request,'pages/practice2.html',context)
def error(request, exception):
    return render(request,'pages/error.html')

   #ham dua qua html
# COURSES
def showCourses(request):
    allCourses=Courses.objects.all().order_by("-date")
    allSubjects=subjects.objects.all()
    context = {'allCourses':allCourses, 'allSubjects':allSubjects}
    return render(request,'pages/courses.html',context)

# hiện thị video cho user
def show_detail_course(request,title):
    try:
        Content=Courses.objects.filter(title=title)
    except Courses.DoesNotExist:
        raise Http404("Practice doesnot exist")
    a=Courses.objects.all()
    context= {'title':title,'question':Content,'a':a}
    return render(request,'pages/coursesVideo.html',context)

# trang hiện thi video cho từng khóa học
def showcourses_detail_demo(request,subject):
    allCourses=Courses.objects.all().order_by("-date")
    allSubjects=subjects.objects.all()
    context= {'subject':subject,'allCourses':allCourses, 'allSubjects':allSubjects}
    return render(request,'pages/basecourses.html',context)
#trang mua 
def seeCourse(request,title):
    a=Courses.objects.all()
    context= {'title':title,'a':a}
    return render(request,'pages/seeCourse.html',context)


#------------------------------------------------------------------------------
# def home(request):
#     allposts = Post.objects.all()
#     totalposts = Post.objects.all().order_by('-date')[:8]
#     context = {'allposts':allposts, 'totalposts':totalposts}
#     return render(request, 'pages/HomePage.html', context)



