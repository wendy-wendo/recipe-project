from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='upload/')
    minutes = models.IntegerField()
    calories = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class SavedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.recipe.name
    

class ShoppingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    qty = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_published = models.DateField(auto_now_add=True)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])

    def __str__(self) -> str:
        return self.comment


class Article(models.Model):
    author = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self) -> str:
        return self.text[:50] + "..."
    