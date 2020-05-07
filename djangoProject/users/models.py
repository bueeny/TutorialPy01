from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# 1 profile = 1 user
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete = models.CASCADE) #models.cascade, delete user = delete this profile too
    birthday =  models.DateField(auto_now = False, auto_now_add = False, null = True)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile-pics',null = True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    
    def __str__ (self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs): # overwrite save function here. To resize image, whens saving this class.
    #     super().save() # Using super for parent attribute

    #     # Upload image > we will grab the image being uploaded. However, it may not be the size that we desire. And also, we need to compress.
    #     # We will need to compress the files into their desired size so that our media won't have any storage issue.
    #     img = Image.open(self.image.path) #Open image from nthe path
        
    #     if (img.height > 300 or img.width > 300):
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path) # This block of code is to overwrite the save method of a model. 