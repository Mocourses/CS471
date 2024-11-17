from django import forms
from ..bookmodule.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']  # Include all fields you need
