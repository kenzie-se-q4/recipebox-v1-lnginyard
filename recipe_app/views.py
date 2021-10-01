from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Recipe, Author
from .forms import AuthorForm, RecipeForm, LoginForm

# Create your views here.


def index(request):
    posts = Recipe.objects.all()
    return render(request, "index.html", {'posts': posts})


def recipe_detail(request, post_id: int):
    form = Recipe.objects.get(id=post_id)
    return render(request, "recipe_detail.html", {"forms": form})


def auth_deets(request, author_id):
    author = Author.objects.get(id=author_id)
    recipe_view = Recipe.objects.filter(author=author)
    return render(request, "author_detail.html", {'author': author,
                                                  'recipe_view': recipe_view})


@login_required
def add_recipe(request, recipe_id):

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeForm()
    return render(request, 'recipe_detail.html', {'form': form})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            myuser = User.objects.create_user(username=data['username'], password=data['password'])
            Author.objects.create(name=data['username'], bio=data['byline'], user=myuser)
            return HttpResponseRedirect(reverse('homepage'))

    form = AuthorForm()
    return render(request, 'auth_deets.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
