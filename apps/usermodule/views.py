from django.shortcuts import render
#LAB_4
from django.http import HttpResponse

from ..static import forms 
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# from .models import Book
# from .models import Student, Student2
# from .models import Address, Address2, ImageGallery

from django.contrib.auth.models import User

# Create your views here.
def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, " bookmodule/index.html" , {"name": name})

def index2(request, val1 ): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

 #LAB11
 #LAB 11
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('login')  # Redirect to login page
    return render(request, 'users/register.html')   

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('student_list')  # Replace 'home' with the name of your main page view
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')  # Redirect to login page after logging out