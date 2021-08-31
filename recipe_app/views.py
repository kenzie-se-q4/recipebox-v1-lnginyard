from django.shortcuts import render
from recipe_app.models import Author, Recipe
from django.http import HttpResponseRedirect

from recipe_app.forms import AuthorForm, RecipeForm


def index(request):
        recipe_view = Recipe.objects.all()
        return render(request, 'index.html', {'recipe': recipe_view})

def add_author(request):
        form = AuthorForm(request.POST, request.FILES)
        return render(request, 'author.html', {'form': form})


def add_recipe(request):
        form = RecipeForm(request.POST, request.FILES)
        return render(request, 'recipe.html', {'form': form})


def recipe_detail(request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, author_id):
        view_author = Author.objects.get(id=author_id)
        author_recipe = Recipe.objects.filter(author=view_author)
        return render(request, 'author_detail.html', {'author': view_author, 'recipe': author_recipe})
