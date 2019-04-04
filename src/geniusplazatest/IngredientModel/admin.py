from django.contrib import admin

# Register your models here.

from .models import IngredientModel

admin.site.register(IngredientModel)