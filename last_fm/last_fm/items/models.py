from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
	id_art = models.CharField(blank=True,primary_key=True,max_length=255)
	name_art = models.CharField(('name_art'),blank=True, max_length=255)
	def _str_(self):
		return"()".format(self.name_art)

class Items(models.Model):
	id_item = models.CharField(blank=True,primary_key=True,max_length=255)
	id_art = models.ForeignKey(Artist,related_name="id_artista_items",on_delete=models.CASCADE)
	name_item = models.CharField(('name_item'),blank=True, max_length=255)
	def _str_(self):
		return"()".format(self.name_item)

class Picture_item(models.Model):
	id_item = models.ForeignKey(Items,related_name="picture_items",on_delete=models.CASCADE)
	picture_item = models.ImageField(upload_to = "item_picture")
	def _str_(self):
		return"()".format(self.id_item)

class Picture_art(models.Model):
	id_art = models.ForeignKey(Artist,related_name = "picture_artist",on_delete=models.CASCADE)
	picture_art = models.ImageField(upload_to = "artist_picture")
	def _str_(self):
		return"()".format(self.id_art)

class tx_item(models.Model):
	#id_user = models.ForeignKey(User,related_name = "tx_user",on_delete=models.CASCADE)
	id_art = models.ForeignKey(Artist,related_name = "tx_artist",on_delete=models.CASCADE)
	id_item = models.ForeignKey(Items,related_name="tx_items",on_delete=models.CASCADE)
	date_tx =  models.DateTimeField(auto_now=True)
	def _str_(self):
		return"()".format(self.id_art,self.id_item)



class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return username"""
        return self.user