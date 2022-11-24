from django.db import models
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.
class Project(models.Model):

    projectId = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=150,blank=False)
    description = models.TextField(blank=False)
    year = models.IntegerField(blank=False,validators=[MinValueValidator(1900),MaxValueValidator(datetime.datetime.now().year)])
    mentor = models.CharField(max_length=100,blank=False)
    youtubeLink = models.URLField(max_length=200,default='')
    category  = models.CharField(max_length=100,blank=False)



    def __str__(self):
        return self.name

class teamDetails(models.Model):
    roll = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    projectId = models.CharField(max_length=20,blank=False)


    def __str__(self):
        return "Team " + self.projectId + " " + self.name

class postLikes(models.Model):
    macAddress = models.CharField(max_length=20,primary_key=True)
    projectId = models.CharField(max_length=20)
