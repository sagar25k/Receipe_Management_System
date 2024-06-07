import requests
from django.db import models

class BeveragesRecipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.image_url:
            self.image_url = self.get_image()
        super().save(*args, **kwargs)

    def get_image(self):
        # Fetch an image from an external source
        response = requests.get('https://source.unsplash.com/400x300/?beverage')
        return response.url

    def __str__(self):
        return self.title
