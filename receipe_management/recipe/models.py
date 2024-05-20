from django.db import models
from django.utils import timezone

class RecipeType(models.Model):
  """
  Model for storing different recipe types (e.g., Dessert, Appetizer)
  """
  name = models.CharField(max_length=200)

  def __str__(self):
    return f"RecipeType {self.name}"

class Recipe(models.Model):
  """
  Model for storing recipe information
  """
  name = models.CharField(max_length=200)
  description = models.TextField()
  prep_time = models.DurationField(blank=True, null=True)  # Optional prep time
  cook_time = models.DurationField(blank=True, null=True)  # Optional cook time
  servings = models.IntegerField()
  instructions = models.TextField()
  recipe_type = models.ForeignKey(RecipeType, on_delete=models.CASCADE)  # Link to recipe type
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"Recipe {self.name}"