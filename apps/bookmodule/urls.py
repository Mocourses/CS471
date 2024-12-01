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

#lab7

path('simple/query', views.simple_query),
path('complex/query', views.complex_query),


#lab8
path('lab8/task1', views.task1),
path('lab8/task2', views.task2),
path('lab8/task3', views.task3),
path('lab8/task4', views.task4),
path('lab8/task5', views.task5),
path('lab8/task7', views.task7),

#lab9
path('lab9_part1/listbooks', views.lab9_part1, name='lab9_part1'), 
path('lab9_part1/addbook', views.addbook),
path('lab9_part1/editbook/<id>', views.editbook),
path('lab9_part1/deletebook/<id>', views.deletebook),

#lab9_part2
path('lab9_part2/listbooks', views.lab9_part2, name='lab9_part2'),
path('lab9_part2/addbook', views.addbook_form, name='addbook_form'),
path('lab9_part2/editbook/<int:id>', views.editbook_form, name='editbook_form'),
# path('books/lab9_part2/deletebook/<int:id>', views.deletebook_form, name='deletebook_form'),

#LAB10 
path('students/', views.student_list, name='student_list'),
path('students/add/', views.student_add, name='student_add'),
path('students/<int:id>/update/', views.student_update, name='student_update'),
path('students/<int:id>/delete/', views.student_delete, name='student_delete'),

path('students2/', views.student2_list, name='student2_list'),
path('students2/add/', views.student2_add, name='student2_add'),
path('students2/<int:id>/update/', views.student2_update, name='student2_update'),
path('students2/<int:id>/delete/', views.student2_delete, name='student2_delete'),

path('images/', views.image_gallery_list, name='image_gallery_list'),
path('images/upload/', views.image_gallery_upload, name='image_gallery_upload'),

#LAB12
path('lab12/task1', views.lab12_task1, name='lab12_task1'),
path('lab12/task2', views.lab12_task2, name='lab12_task2'),
path('lab12/task3', views.lab12_task3, name='lab12_task3'),
path('lab12/task4', views.lab12_task4, name='lab12_task4'),
path('lab12/task5', views.lab12_task5, name='lab12_task5'),

]
