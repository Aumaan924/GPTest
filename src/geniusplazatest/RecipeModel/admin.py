from django.contrib import admin

# Register your models here.

from .models import RecipeModel

admin.site.register(RecipeModel)