from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User
from django.shortcuts import get_object_or_404
from PIL import Image, ImageOps


# Create your models here.
class Customer(models.Model):
    customerID = models.ForeignKey(User ,on_delete = models.CASCADE) #models.cascade, delete user = delete this profile too

    def __str__ (self):
        return self.customerID

class ProductClassification(models.Model):
    productClassification = models.CharField(max_length = 30, null = False,  unique=True)

    def __str__ (self):
        return self.productClassification

class CurrencyList(models.Model):
    currencyType = models.CharField(max_length = 3, null = False, unique = True)
    currencyMultiplier = models.FloatField(null = False)

    def __str__ (self):
        return self.currencyType

    # Upper Case
    def save(self, *args, **kwargs):
        self.currencyType = self.currencyType.upper()
        return super(CurrencyList, self).save(*args, **kwargs)

class Product(models.Model):
    productName = models.CharField(max_length = 200, null = False)
    priceCurrency = models.ForeignKey(CurrencyList, on_delete = models.PROTECT, default = None, to_field = 'currencyType') #Price currency
    productPrice = models.FloatField()
    productCategory = models.ForeignKey(ProductClassification, on_delete = models.PROTECT, related_name='products')
    productDescription = models.TextField(blank = True)
    image = models.ImageField(default = 'default.jpg', upload_to = 'product-pics',blank=True) 
    date_posted = models.DateTimeField(default =  timezone.now)
    
    def __str__ (self):
        return self.productName

    # def save(self, *args, **kwargs): # overwrite save function here. To resize image, whens saving this class.
    #     super().save(*args, **kwargs) # Using super for parent attribute

    #     img = Image.open(self.image.path) #Open image from nthe path
        
    #     if (img.height > 500 or img.width > 500):
    #         basewidth = 500
    #         wpercent = (basewidth/float(img.size[0]))
    #         hsize = int((float(img.size[1])*float(wpercent))) # maintain aspect ratio
    #         output_size = (basewidth,hsize) # maintain aspect ratio
    #         img.thumbnail(output_size, Image.ANTIALIAS)
    #         img.save(self.image.path) # This block of code is to overwrite the save method of a model.

        # each object will coresspond to one url
    def get_absolute_url(self):
        return reverse('store-home', kwargs= {'pk':self.productName.pk}) 