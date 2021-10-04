from django.shortcuts import render
from recipe_app.models import Author, Recipe
from recipe_app.forms import AuthorForm, RecipeForm


def index(request):
    recipe_view = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipe_view})


def add_author(request):
    form = AuthorForm(request.POST, request.FILES)
    return render(request, 'author.html', {'form': form})


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_vaid():
            data = form.cleaned_data
            author _ Recipe.objects.create(
                title=data.get("title")
                author=data.get("author")
                description=data.get("description"),
                time_required=data.get("time_required"),
                instructions=data.get("instructions"),
            )
            return HttpResponseRedirect(reverse("homepage")) 
else:
    form = AddRecipeForm()

return render(request, "", {"form": form})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def auth_deets(request, author_id):
    author = Author.objects.get(id=author_id)
    recipe = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'recipe': recipe})
