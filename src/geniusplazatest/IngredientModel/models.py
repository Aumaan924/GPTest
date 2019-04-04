from django.db import models
from RecipeModel.models import RecipeModel

# Create your models here.
class IngredientModel(models.Model):
	text = models.CharField(max_length=255, default='')
	IRecipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, default=1)