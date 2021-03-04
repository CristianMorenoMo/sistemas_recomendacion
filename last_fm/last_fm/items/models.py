from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Artist(models.Model):
    artid = models.CharField(max_length=200,null=True,unique=True)
    name_art = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return "%s" % (self.name_art)


class Item(models.Model):
    traid = models.CharField(max_length=200,null=True,unique=True)
    traname = models.CharField(max_length=200,null=True)
    artist = models.ForeignKey(Artist,max_length=500,on_delete=models.CASCADE,default='DEFAULT VALUE')
    
    def __str__(self):
        return "%s" % (self.name_item)



class Picture(models.Model):
    item = models.OneToOneField(Item,max_length=500,on_delete=models.CASCADE,default='DEFAULT VALUE')
    image = models.ImageField(upload_to='imagenes_producto')
    def __str__(self):
        return "%s" % (self.item)




class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return username"""
        return "{}".format(self.user)