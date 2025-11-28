from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
