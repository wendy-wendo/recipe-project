from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import RecipeForm, IngredientForm, ShoppingForm, ReviewForm, ArticleForm
from .models import Recipe, Ingredient, SavedRecipe, ShoppingItem, Review, Article

# Create your views here.
def index(request):
    return render(request, 'recipeApp/index.html')


def add_recipe(request):
    if request.method != 'POST':
        form = RecipeForm()

    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.uploader = request.user
            new_recipe.save()

        return redirect('recipeApp:recipes')
    
    context = {'form': form}
    return render(request, 'recipeApp/add_recipe.html', context)


def recipes(request):
    all_recipes = Recipe.objects.all()
    context = {'recipes': all_recipes}
    return render(request, 'recipeApp/recipes.html', context)


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    saved_recipes = SavedRecipe.objects.filter(recipe=recipe, user=request.user)
    reviews = Review.objects.filter(recipe=recipe)

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.recipe = recipe
            new_review.save()

        return redirect('recipeApp:recipe', recipe.id)
    
    else:
        form = ReviewForm()

    context = {'recipe': recipe, 'ingredients': ingredients, 'reviews':reviews, 'saved_recipes': len(saved_recipes), 'form': form}
    return render(request, 'recipeApp/recipe.html', context)


def add_ingredient(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method != 'POST':
        form = IngredientForm()

    else:
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            new_ingredient = form.save(commit=False)
            new_ingredient.recipe = recipe
            new_ingredient.save()
        
        return redirect('recipeApp:recipe', recipe.id)
    
    context = {'form': form}
    return render(request, 'recipeApp/add_ingredient.html', context)


def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']

        recipes = Recipe.objects.filter(
            Q(tag__name__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(owner__icontains=search_query)
        )
        context = {'recipes': recipes}
        return render(request, 'recipeApp/recipes.html', context)

    else:
        return render(request, 'recipeApp/recipes.html',{})
    

def save_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    is_saved = len(SavedRecipe.objects.filter(recipe=recipe, user=request.user))
    if not is_saved:
        new_saved_recipe = SavedRecipe(recipe=recipe, user=request.user)
        new_saved_recipe.save()

    return redirect('recipeApp:recipe', recipe.id)


def saved_recipes(request):
    saved_recipes = SavedRecipe.objects.filter(user=request.user)
    context = {'saved_recipes': saved_recipes}
    return render(request, 'recipeApp/saved_recipes.html', context)


def shopping_list(request):
    shopping_items = ShoppingItem.objects.filter(user=request.user)
    context = {'shopping_items': shopping_items}
    return render(request, 'recipeApp/shopping_list.html', context)


def add_shopping_item(request):
    if request.method != 'POST':
        form = ShoppingForm()

    else:
        form = ShoppingForm(data=request.POST)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

        return redirect('recipeApp:shopping_list')
    
    context = {'form': form}
    return render(request, 'recipeApp/add_shopping_item.html', context)


def delete_shopping_item(request, item_id):
    shopping_item = ShoppingItem.objects.get(id=item_id)
    shopping_item.delete()
    return redirect('recipeApp:shopping_list')


def ingredients_to_shopping(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = recipe.ingredients.all()
    
    for ingredient in ingredients:
        item, created = ShoppingItem.objects.get_or_create(user=request.user, name=ingredient.name)

    return redirect('recipeApp:shopping_list')


def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    recipe = review.recipe
    review.delete()
    return redirect('recipeApp:recipe', recipe.id)


def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    recipe = review.recipe

    if request.method != 'POST':
        form = ReviewForm(instance=review)

    else:
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.recipe = recipe
            new_review.save()

        return redirect('recipeApp:recipe', recipe.id)
    
    context = {'form': form, 'recipe': recipe, 'review': review}
    return render(request, 'recipeApp/edit_review.html', context)


def articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'recipeApp/articles.html', context)


def add_article(request):
    if request.method != 'POST':
        form = ArticleForm()

    else:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('recipeApp:articles')
    
    context = {'form': form}
    return render(request, 'recipeApp/add_article.html', context)


def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('recipeApp:articles')


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method != 'POST':
        form = ArticleForm(instance=article)

    else:
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
        
        return redirect('recipeApp:articles')
    
    context = {'form': form, 'article': article}
    return render(request, 'recipeApp/edit_article.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    paragraphs = article.text.split('\n')
    context = {'article': article, 'paragraphs': paragraphs}
    return render(request, 'recipeApp/article.html', context)
