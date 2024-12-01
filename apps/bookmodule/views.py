from django.shortcuts import render
#LAB_4
from django.http import HttpResponse

#LAB 7
from django.db import models  # Import models

from .models import Book
from .models import Student, Student2
from .models import Address, Address2, ImageGallery

#lab8
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min

from django.shortcuts import redirect
from ..static import forms 
from django.contrib import messages

from django.contrib.auth.decorators import login_required







# #LAB_4
# def index(request):
#  return HttpResponse("Hello, world!")

# #LAB_4
# def index(request):
#  name = request.GET.get("name") or "world!" #add this line
#  return HttpResponse("Hello, "+name) 

# #LAB_4
# def index(request):
#  name = request.GET.get("name") or "world!"
#  return render(request, "bookmodule/index.html")

#LAB_4
def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "bookmodule/index.html" , {"name": name})

def index2(request, val1 ): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)


#Lab_4
def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

#lab_5
def links(request):
 return render(request, 'bookmodule/links.html')
def formatting(request):
 return render(request, 'bookmodule/formatting.html')
def listing(request):
 return render(request, 'bookmodule/listing.html')
def tables(request):
 return render(request, 'bookmodule/tables.html')

#lab6
def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]
# will be called twice based on what request method
# if method == post then it will be called with the post logic
# else it will be skipped and the rendering of the form will happen
#shows the form template
#listens for POST request, then sends "context dictionoray" to tamplate booklist.html
def lab6(request):
 if request.method == "POST":
    #Post requests comes with form user data in the object "request"
    # collecting the form data
    string = request.POST.get('keyword').lower() #string 
    isTitle = request.POST.get('option1') #boolean
    isAuthor = request.POST.get('option2') #boolean
    
    # This filters the list of books based on the form data.
    books = __getBooksList()
    newBooks = []
    for item in books:
        contained = False
        if isTitle and string in item['title'].lower(): contained = True
        if not contained and isAuthor and string in item['author'].lower():contained = True
        if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList.html', {'books':newBooks})
 return render(request, 'bookmodule/lab6.html')

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='a') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='a').filter(edition__gte = 2).exclude(price__lte = 50)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
    #lab8
def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task2(request):
    # Filter books with edition > 2 and title or author containing 'qu'
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task3(request):
    # Filter books with edition > 2 and title or author containing 'qu'
    books = Book.objects.filter(
        ~Q(edition__gt=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu')
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    # Filter books with edition > 2 and title or author containing 'qu'
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/bookList.html', {'stats': stats})

def task7(request):
    # Annotate to count students in each city
    city_stats = (
        Student.objects
        .values('address__city')  # Group by city
        .annotate(student_count=models.Count('id'))  # Count students
    )

    return render(request, 'bookmodule/students.html', {'city_stats': city_stats})

#lab9
def lab9_part1(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books, 'lab9':True})

def addbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        edition = request.POST.get('edition')
        price = request.POST.get('price')

        # Add other fields as needed
        Book.objects.create(title=title, author=author, price=price, edition=edition )
        books = Book.objects.all().order_by('title')
        return redirect(lab9_part1)
    return render(request, 'bookmodule/addbook.html', {'add':True})

def editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('lab9_part1')
    return render(request, 'bookmodule/addbook.html', {'edit':True, 'book':book})

def deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab9_part1')
   
#lab9 part2
def lab9_part2(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books, 'lab9_part2': True, 'part2':True})

def addbook_form(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lab9_part2')
    else:
        form = forms.BookForm()
    return render(request, 'bookmodule/addbook2.html', {'form': form, 'add': True, 'part2':True})

def editbook_form(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = forms.BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Updates the book record
            return redirect('lab9_part2')
    else:
        form = forms.BookForm(instance=book)  # Pre-fill the form with book data
    return render(request, 'bookmodule/addbook2.html', {'form': form, 'edit': True,'part2':True})

def deletebook_form(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab9_part2')


#Lab10
@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/student_list.html', {'students': students})

@login_required(login_url='login')
def student_add(request):
    if request.method == 'POST':
        student_form = forms.StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('student_list')
    else:
        student_form = forms.StudentForm()
    return render(request, 'bookmodule/student_form.html', {'student_form': student_form})

@login_required(login_url='login')
def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student_form = forms.StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student_list')
    else:
        student_form = forms.StudentForm(instance=student)
    return render(request, 'bookmodule/student_form.html', {'student_form': student_form})

@login_required(login_url='login')
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

#Lab10 #Task 2
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student2_list.html', {'students': students})

def student2_add(request):
    if request.method == 'POST':
        form = forms.Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = forms.Student2Form()
    return render(request, 'bookmodule/student2_form.html', {'form': form})

def student2_update(request, id):
    try:
        student = Student2.objects.get(id=id)
    except Student2.DoesNotExist:
        return redirect('student2_list')

    if request.method == 'POST':
        form = forms.Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = forms.Student2Form(instance=student)
    return render(request, 'bookmodule/student2_form.html', {'form': form})

def student2_delete(request, id):
    try:
        student = Student2.objects.get(id=id)
        student.delete()
    except Student2.DoesNotExist:
        pass
    return redirect('student2_list')

def image_gallery_list(request):
    images = ImageGallery.objects.all()
    return render(request, 'bookmodule/image_gallery_list.html', {'images': images})

def image_gallery_upload(request):
    if request.method == 'POST':
        form = forms.ImageGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_gallery_list')
    else:
        form = forms.ImageGalleryForm()
    return render(request, 'bookmodule/image_gallery_form.html', {'form': form})


#lab12
def lab12_task1(request):
    return render(request, 'bookmodule/lab12_task1.html')
def lab12_task2(request):
    return render(request, 'bookmodule/lab12_task2.html')
def lab12_task3(request):
    return render(request, 'bookmodule/lab12_task3.html')
def lab12_task4(request):
    return render(request, 'bookmodule/lab12_task4.html')
def lab12_task5(request):
    return render(request, 'bookmodule/lab12_task5.html')