# Generated by Django 4.2.4 on 2023-08-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0013_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipeApp.recipe'),
            preserve_default=False,
        ),
    ]