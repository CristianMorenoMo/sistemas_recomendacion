from django.contrib import admin
from .models import Picture,Artist

@admin.register(Picture,Artist)
class AuthorAdmin(admin.ModelAdmin):
	pass

# Register your models here.
