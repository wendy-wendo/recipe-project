from django import forms

from .models import Recipe, Ingredient, ShoppingItem, Review, Article

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['owner', 'name', 'image', 'minutes', 'calories', 'link', 'tag']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name',]


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'qty', ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'topic', 'text', 'image',]
        labels = {'text':''}
        