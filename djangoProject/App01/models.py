from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User
from django.urls import reverse

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length =  100)
    content = models.TextField()
    date_posted = models.DateTimeField(default =  timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__ (self):
        return self.title
    
    # each object will coresspond to one url
    def get_absolute_url(self):
        return reverse('post-detail', kwargs= {'pk':self.pk}) # return the urlpath  as a string so we use reverse

 
