from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
import datetime
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
import GTEAMS_APP
from GTEAMS_APP.models import *
from GTEAMS_APP.form import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='../../accounts/login')
def PageContact(request):
    return render(request,'pages/contact.html')
    
def PagePractice(request):
    return render(request,'pages/practice.html')
def PageBlogs(request):
    return render(request,'pages/blogs.html')
def PageIntro(request):
    return render(request,'pages/intro.html')


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
# CONTACT

def create_contact(request):
    if request.method == 'GET':
        form=CreateNewContact()
    if request.method == 'POST':
        form=CreateNewContact(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'pages/contact.html',{'form':form})
#--------------------------------------------------------------------------
# PRACTICE

def ShowListQuiz(request):
    Question=Quiz.objects.all()
    context = {'question': Question}
    return render(request,'pages/practice.html',context)
def ShowQuiz(request,topic):
    Question=Quiz.objects.get(topic=topic)
    context = {'question': Question}
    return render(request,'pages/practiceQuiz.html',context)
def ShowQuizID(request,topic):
    quiz=Quiz.objects.get(topic=topic)
    questions=[]
    for q in quiz.get_questions():
        answers=[]
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data':questions,
        'time':quiz.time,
    })
def save_quiz_view(request, topic):
    if (request.is_ajax()):
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(topic=topic)

        score = 0
        multiplier = 100 / quiz.numberOfQuestions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.requiredScoreToPass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})

 
#---------------------------------------------------------------------------------------------------------------
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
    allSubjects=subjects.objects.all()
    context= {'title':title,'a':a, 'allSubjects':allSubjects}
    return render(request,'pages/seeCourse.html',context)

cart ={}
def addCart(request):
    if request.is_ajax():
        id=request.POST.get('id')
        num=request.POST.get('num')
        coDetail = Courses.objects.get(id=id)
        user=request.user
        if id in cart.keys():
            itemCart={
                'name':coDetail.title,
                'price':int(coDetail.costReal),
                'image':str(coDetail.image),
                'num': int(cart[id]['num']) +1,
            }
        else:
            itemCart={
                'name':coDetail.title,
                'price':int(coDetail.costReal),
                'image':str(coDetail.image), 
                'num': num,
            }
        cart[id]=itemCart
        request.session['cart']=cart
        cartInfo=request.session['cart']
        context= {'cart':cartInfo}
        Cart.objects.create(title=coDetail, user=user, paid=False)
        
        return render(request,'pages/addCart.html', context)
    else:
        return render(request,'pages/addCart.html')

def cartShopping(request):
    user=request.user
    cart2=Cart.objects.filter(user=user)
    context= {'cart':cart2}
    return render(request,'pages/cart.html',context)

def detailCart(request):
    return render(request,'pages/detailCart.html')
#------------------------------------------------------------------------------
# def home(request):
#     allposts = Post.objects.all()
#     totalposts = Post.objects.all().order_by('-date')[:8]
#     context = {'allposts':allposts, 'totalposts':totalposts}
#     return render(request, 'pages/HomePage.html', context)


def blogHome(request): 
    allPosts= article_blog.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'pages/blogHome.html', context)

def blogPost(request, slug): 
    post=article_blog.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "pages/blogPost.html", context)

def quizHome(request): 
    allPosts= article_quiz.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'pages/quizsHome.html', context)

def quizPost(request, slug): 
    post=article_quiz.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "pages/quizsPost.html", context)



