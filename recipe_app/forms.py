from django import forms
from recipe_app.models import Author


# form to add new recipe
# form to add  new author


class AuthorForm(forms.Form):
    name = forms.CharField(label="Author", max_length=100)
    bio = forms.CharField(label="Bio")


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    cook_time = forms.CharField(max_length=25)
    instructions = forms.CharField(widget=forms.Textarea)
