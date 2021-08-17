from django import forms
from django.forms import ModelForm
from recipe_app.models import Author, Recipe

# form to add new recipe
# form to add  new author


class AuthorForm(forms.ModelForm):
    name = forms.CharField(label="Author", max_length=100)
    bio = forms.CharField(label="Bio")

class RecipeForm(forms.Form):
        description = forms.CharField(widget=forms.Textarea)
        title = forms.ModelChoiceField(queryset=Author.objects.all())
        time_required = forms.CharField(max_length=30)
        instructions = forms.CharField(widget=forms.Textarea)
        author = forms.CharField(max_length=50)

 #class AuthorForm(forms.ModelForm):
         # """ """