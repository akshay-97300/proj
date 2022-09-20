from django.shortcuts import render
from django.views.generic.list import ListView
from .models import User
from django.views import generic
from django.db import connection


class UserListView(generic.ListView):
    model = User
    context_object_name = 'users'   # your own name for the list as a template variable
    #queryset = User.objects.all()# Get 5 books containing the title war
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM users_user WHERE first_name = "akshay"''')
    template_name = 'user.html'  # Specify your own template name/location


class UserView(generic.ListView):
    model = User
    context_object_name = 'users'   # your own name for the list as a template variable
    #queryset = User.objects.all()# Get 5 books containing the title war
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM users_user WHERE first_name = "akshay"''')
    template_name = 'user.html'  # Specify your own template name/location
