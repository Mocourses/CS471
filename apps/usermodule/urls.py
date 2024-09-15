from django.urls import path
from . import views

#LAB_4
urlpatterns = [
 path('', views.index),
 path('index2/<int:val1>/', views.index2),
#  path('<int:bookID>', views.viewbook)
]
