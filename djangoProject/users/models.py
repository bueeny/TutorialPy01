from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 1 profile = 1 user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #models.cascade, delete user = delete this profile too
    birthday =  models.DateField()
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile-pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    
    def __str__ (self):
        return f'{self.user.username} Profile'
