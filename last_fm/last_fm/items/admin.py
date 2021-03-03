from django.contrib import admin
from .models import Items,Picture_item

@admin.register(Items,Picture_item)
class AuthorAdmin(admin.ModelAdmin):
	pass

# Register your models here.
