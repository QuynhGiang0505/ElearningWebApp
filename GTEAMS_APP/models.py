from django.db import models

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
from embed_video.fields import EmbedVideoField
class Courses(models.Model):
    title=models.CharField(primary_key=True, max_length=100)
    author = models.CharField(max_length=50)
    linkVideo = EmbedVideoField()
    added = models.DateTimeField(auto_now_add=True)
    MieuTa=models.TextField()
    subject = models.CharField(max_length=100)
    cost = models.IntegerField(null=True, blank=True)
    costReal = models.CharField(max_length=20, null=True, blank=True)
    #image = models.FileField(upload_to='images/', blank=True, null=True)
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



