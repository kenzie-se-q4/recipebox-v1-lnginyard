from django.shortcuts import render
from recipe_app.models import Author, Recipe
# Create your views here.


def index(request):
    recipe_view = Recipe.objects.all()
    return render(request, 'index.html', {'recipe_view': recipe_view})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, author_id):
    view_author = Author.objects.get(id=author_id)
    author_recipes = Recipe.objects.filter(author=view_author)
    return render(request, 'author_detail.html', {'author': view_author, 'recipes': author_recipes})
