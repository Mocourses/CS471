from django.urls import path
from . import views

#LAB_4
urlpatterns = [
 path('', views.index),
 path('index2/<int:val1>/', views.index2),
 path('register/', views.register, name='register'),
 path('login/', views.login_view, name='login'),
 path('logout/', views.logout_view, name='logout'),

]
