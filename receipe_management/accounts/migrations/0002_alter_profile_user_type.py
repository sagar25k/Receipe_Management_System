# Generated by Django 5.0.6 on 2024-05-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('recipe_manager', 'Recipe Manager'), ('cook', 'Cook'), ('editor', 'Editor'), ('admin', 'Admin')], max_length=20),
        ),
    ]
