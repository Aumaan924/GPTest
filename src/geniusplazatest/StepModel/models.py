from django.db import models
from RecipeModel.models import RecipeModel

# Create your models here.
class StepModel(models.Model):
	step_text = models.TextField(max_length=255, default='')
	SRecipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, default=1)