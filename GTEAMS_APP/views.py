from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
import datetime
from django.http import HttpResponse
from icecream import ic
import GTEAMS_APP
from GTEAMS_APP.models import *
from GTEAMS_APP.form import *
# Create your views here.
def PageHome(request):
    return render(request, 'pages/HomePage.html',{'now':datetime.datetime.now()})
def PageContact(request):
    return render(request,'pages/contact.html')
def PagePractice(request):
    return render(request,'pages/practice.html')
def PageBlog(request):
    return render(request,'pages/blogs.html')
def PageLogin(request):
    return render(request,'pages/login.html')
def PageRegister(request):
    return render(request,'pages/register.html')
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
