from django.db import models
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.
class Project(models.Model):

    projectId = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20,blank=False)
    description = models.TextField(max_length=250,blank=False)
    year = models.IntegerField(blank=False,validators=[MinValueValidator(1900),MaxValueValidator(datetime.datetime.now().year)])
    mentor = models.CharField(max_length=50,blank=False)
    category  = models.CharField(max_length=20,blank=False)



    def __str__(self):
        return self.name

