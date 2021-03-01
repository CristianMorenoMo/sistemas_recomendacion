from django.contrib import admin
from .models import Items, Artist,Picture_item,Picture_art,tx_item

@admin.register(Items,Artist,Picture_item,Picture_art,tx_item)
class AuthorAdmin(admin.ModelAdmin):
	pass

# Register your models here.
