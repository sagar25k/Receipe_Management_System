from django.db import models
import requests

class SeafoodRecipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.image_url:
            self.image_url = self.get_image()
        super().save(*args, **kwargs)

    def get_image(self):
        # Fetch an image from an external source
        response = requests.get('https://images.pexels.com/photos/262959/pexels-photo-262959.jpeg')
        return response.url

    def __str__(self):
        return self.title
