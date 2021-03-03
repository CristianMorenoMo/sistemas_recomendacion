from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Items(models.Model):
	name_item = models.CharField(('name_item'),blank=True, max_length=255)
	name_art = models.CharField(('name_art'),blank=True, max_length=255)

	def __str__(self):
		return"{}".format(self.name_item)

class Picture_item(models.Model):
    picture_item = models.ImageField(upload_to = "item_picture")
    item = models.ForeignKey(Items,related_name="picture_items",on_delete=models.CASCADE)
    
    def __str__(self):
        return"{}".format(self.item)





class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return username"""
        return "{}".format(self.user)