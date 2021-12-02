import django
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
class Contact(models.Model):
 
    name = models.CharField(max_length=200)

    email=models.EmailField(max_length=200)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class Quiz(models.Model):
    name=models.CharField(max_length=50)
    topic=models.CharField(max_length=200)
    numberOfQuestions=models.IntegerField()
    time=models.IntegerField(help_text="thời gian làm bài tính bằng phút")
    requiredScoreToPass=models.IntegerField(help_text="điểm số cần để hoàn thành bài kiểm tra")
    def __str__(self):
        return f"{self.name}-{self.topic}"
    def get_questions(seft):
        return seft.question_set.all()
    class Meta:
        verbose_name_plural='Quizes'
    
class Question(models.Model):   
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,)
    text=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.text)
    def get_answers(seft):
        return seft.answer_set.all()
class Answer(models.Model):
    text=models.CharField(max_length=200)
    correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"question: {self.question}, answer:{self.text},correct:{self.correct}"
class Result(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)        
    """ user la foreinkey cuar class user """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.FloatField()
    def __str__(self):
        return str(self.pk)

#Courses
class typeCourse(models.Model):
    Type=models.CharField(max_length=10)
    def __str__(self):
        return self.Type

class subjects(models.Model):
    subjectName = models.CharField(max_length=100)
    def __str__(self):
        return self.subjectName 

from embed_video.fields import EmbedVideoField
class Courses(models.Model):
    title=models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    linkVideo = EmbedVideoField()
    added = models.DateTimeField(auto_now_add=True)
    MieuTa=models.TextField()
    # subject = models.CharField(max_length=100)
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE)
    Type=models.ForeignKey(typeCourse, on_delete=models.CASCADE)
    costReal = models.CharField(max_length=20, null=True, blank=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-added'] 


    


class Post(models.Model):
    title = models.CharField(max_length=500)
    meta_tags = models.CharField(max_length=2000, blank=True)
    meta_desc = models.TextField(max_length=2000, blank=True)

    #image = models.ImageField(upload_to='media/post')
    image_alt_name = models.CharField(max_length=200, blank=True)
    #desc = RichTextField(blank=True, null=True)

    youtube = models.URLField(max_length=500, default='' )
    author = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    

    def __str__(self):
       return self.title

class article_quiz(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

class article_blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

#-------------------------------------------------------------
class cartUser(models.Model):
    username=models.ForeignKey(subjects, on_delete=models.CASCADE)
    masp=models.IntegerField(default=0)
    subject=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    costReal = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.username
    



