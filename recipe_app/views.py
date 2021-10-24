from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Author, Recipe
from recipe_app.forms import AuthorForm, RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name = data['name'],
                bio = data['bio']
            )
        return HttpResponseRedirect(reverse('Home'))
    form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                cook_time=data["cook_time"],
                instructions=data["instructions"],
            )
        return HttpResponseRedirect(reverse("Home"))
    form = RecipeForm()
    return render(request, "add_recipe.html", {"form": form})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def auth_deets(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author,
                                                  'recipe': recipe})
