from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.forms import AddRecipe, AuthorForm
from homepage.models import Recipe, Author

# Create your views here.

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "welcome_name": "SE-9"})

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {'post': my_recipe})

def recipe_list(request, id):
    authors = Author.objects.all().filter(id=id)
    items = Recipe.objects.all().filter(author_id=id)
    return render(request, "recipe_list.html", {'recipes': items, "authors": authors})

def recipe_form(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get('title'),
                body = data.get('body'),
                author = data.get('author')
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddRecipe()
    return render(request, "recipe_and_author_forms.html", {"form": form})

def author_form(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AuthorForm()
    return render(request, "recipe_and_author_forms.html", {'form': form})

"""
localhost:8000/
localhost:8000/post/3
"""