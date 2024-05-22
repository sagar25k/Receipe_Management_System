from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPES = (
        ('recipe_manager', 'Recipe Manager'),
        ('cook', 'Cook'),
        ('editor', 'Editor'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.user.username}'s Profile"
