from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='recipeApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipe/<int:recipe_id>/add_ingredient', views.add_ingredient, name='add_ingredient'),
    path('search/', views.search, name='search'),
    path('save_recipe/<int:recipe_id>/', views.save_recipe, name='save_recipe'),
    path('saved_recipes', views.saved_recipes, name='saved_recipes'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('add_shopping_item', views.add_shopping_item, name='add_shopping_item'),
    path('delete_shopping_item/<int:item_id>/', views.delete_shopping_item, name='delete_shopping_item'),
    path('ingredients_to_shopping/<int:recipe_id>/', views.ingredients_to_shopping, name='ingredients_to_shopping'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
