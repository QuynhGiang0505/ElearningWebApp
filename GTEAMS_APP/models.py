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
