# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            todo_lists = List.objects.all
            messages.success(request, ('Item SuccessFully Added to List!'))
            return render(request, 'home.html', {'todo_lists': todo_lists})
    else: 
        todo_lists = List.objects.all
        return render(request, 'home.html', {'todo_lists': todo_lists})

def about(request):
    data = {'first_name': 'Vivek', 'last_name': 'Rajyaguru'}
    return render(request, 'about.html', data)