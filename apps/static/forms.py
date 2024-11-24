from django import forms
from ..bookmodule.models import Book, Student, Address, Student2, Address2, ImageGallery

#LAB11
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']  # Include all fields you need

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']

class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ['title', 'image']


#LAB 11
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']