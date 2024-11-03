from django.shortcuts import render
#LAB_4
from django.http import HttpResponse

#LAB 7
from django.db import models  # Import models

from .models import Book
from .models import Student
from .models import Address

#lab8
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min

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