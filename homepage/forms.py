from django import forms
from homepage.models import Recipe, Author

class AddRecipe(forms.Form):
    title = forms.CharField(max_length = 50)
    body = forms.CharField(widget = forms.Textarea)
    author = forms.ModelChoiceField(queryset = Author.objects.all())

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]