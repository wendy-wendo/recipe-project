# Generated by Django 4.2.4 on 2023-08-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0015_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]