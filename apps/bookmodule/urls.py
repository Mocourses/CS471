from django.urls import path
from . import views

#LAB_4
urlpatterns = [
 path('', views.index),
 path('index2/<int:val1>/', views.index2),
 path('<int:bookId>', views.viewbook),

 #Lab_4
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),

#lab 5
path('html5/links', views.links),
path('html5/text/formatting', views.formatting),
path('html5/listing', views.listing),
path('html5/tables', views.tables),

#lab 6
# listens for get or post requests.
path('search/', views.lab6),

]
