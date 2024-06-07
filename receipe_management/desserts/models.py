from django.db import models
import requests

class DessertRecipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    ingredients = models.TextField(help_text="List each ingredient on a new line")
    instructions = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.image_url:
            self.image_url = self.get_image_url()
        super().save(*args, **kwargs)

    def get_image_url(self):
        response = requests.get(f'https://source.unsplash.com/400x300/?{self.category}')
        return response.url
