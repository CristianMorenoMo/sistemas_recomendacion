from django.contrib import admin
from .models import Item,Picture,Artist

@admin.register(Item,Picture,Artist)
class AuthorAdmin(admin.ModelAdmin):
	pass

# Register your models here.
