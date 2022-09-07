from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Projects informations

class Projects(models.Model):
    agix_manager=models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=200)
    project_description = models.TextField(blank=True , null=True)
    project_image = models.ImageField(null =True , blank = True, upload_to='images' , default='house-icon-png-17.png')
    complete = models.BooleanField(default =True)
   

    def __str__(self):
        return self.project_name
    
    def __str__(self):
        return self.client_name

# Staff ingformations

class Staff(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_major = models.CharField(max_length=50)
    employee_description = models.TextField(blank=True , null=True)
    employee_previous_project = models.ManyToManyField(Projects,related_name='participants',blank=True)
    employee_profile_picture = models.ImageField(null =True , blank = True, upload_to='images' , default='Employee__business_man.png')

    def __str__(self):
        return self.employee_name
    
    def __str__(self):
        return self.employee_major

class Major_skills(models.Model):
    employee = models.ForeignKey(Staff,on_delete=models.CASCADE)
    skills = models.CharField(max_length=50)

    def __str__(self):
        return self.skills
    
    
    
