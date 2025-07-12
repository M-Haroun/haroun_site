from django.db import models
from datetime import datetime
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=50,blank=False, null= False)
    email = models.EmailField(blank=False, null= False)
    phone = models.CharField(max_length=15,blank=True, null= True)
    message = models.TextField(max_length=200,blank=False, null= False)
    posted = models.DateTimeField(default=datetime.now(),blank=True, null= True)
    
    def __str__(self):
            return self.name
    
    class Meta:
        ordering = ['posted']