from django.db import models
from django.db.models.base import Model

class Contact(models.Model):
 
    name = models.CharField(max_length=200)

    email=models.EmailField(max_length=200)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=1000)
    def __str__(self):
        return self.title
class Practice_title(models.Model):
    title=models.CharField(primary_key=True,max_length=50)
    title_Content=models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Practice(models.Model):   
    title=models.ForeignKey(Practice_title,on_delete=models.CASCADE)
    question=models.CharField(max_length=200)
    contentA=models.CharField(max_length=500)
    contentB=models.CharField(max_length=500)
    contentC=models.CharField(max_length=500)
    contentD=models.CharField(max_length=500)
    correctAnswer=models.CharField(max_length=500,null=True)
    c=models.ManyToManyField
    def __str__(self):
            return self.question


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

class article(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author


