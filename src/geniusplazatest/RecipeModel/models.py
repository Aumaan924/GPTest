from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RecipeModel(models.Model):
	Name = models.CharField(max_length=255, default='')
	Author = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, default=1)