from django.db import models
from datetime import datetime

# Create your modsels here.

# Make flexable adding categories for projects and if I make new project that belongs to 
# new category I can add its new one 

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True, null= True)
    
    def __str__(self):
        return self.name

# Add technologies that used in project with this method due to make add new technologies
# for new projects easy and flexable
    
class Technology(models.Model):
    tech_name  = models.CharField(max_length=100,blank=True, null= True)
    
    def __str__(self):
        return self.tech_name

# Make projects table   
class Project(models.Model):
    project_status = [
        ('Completed','Completed'),
        ('Work on','Work on'),
    ]
    
    title = models.CharField(max_length=200,blank=False, null= False)
    description = models.TextField(max_length=700,blank=False, null= False)
    category = models.ForeignKey(Category,null=True,  blank=True, on_delete=models.PROTECT)
    main_img = models.ImageField(upload_to='photos/main_project_photos', null=False,  blank=False)
    Technologies = models.ManyToManyField(Technology,null=True,  blank=True) 
    link = models.URLField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=50, null=True,  blank=True, choices= project_status)
    updated = models.DateTimeField(default=datetime.now(),blank=True, null= True)
    
    def __str__(self):
        return self.title
    
    
#To add more image for one project
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='photos/project_photos', null=True,  blank=True)    