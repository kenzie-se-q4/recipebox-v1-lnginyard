from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Author, Recipe
from recipe_app.forms import AuthorForm, RecipeForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


@staff_member_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=user
            )
        return HttpResponseRedirect(reverse('Home'))
    form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


@login_required
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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('Home')))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    html = "logout_view.html"
    logout(request)
    messages.info(request, "Sad to see you go")
    return HttpResponseRedirect(reverse('Home'))


