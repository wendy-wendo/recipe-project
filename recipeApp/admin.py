from django.contrib import admin

from .models import Tag, Recipe, Ingredient, SavedRecipe, Review, Article

# Register your models here.
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(SavedRecipe)
admin.site.register(Review)
admin.site.register(Article)
