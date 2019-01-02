# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

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

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Deleted SuccessFully!'))
    return redirect('home')

def updatestatus(request, list_id, flag):
    item = List.objects.get(pk=list_id)
    if flag == 1:
        item.completed = True
    else:
        item.completed = False
    item.save()
    messages.success(request, ('Item Updated SuccessFully!'))
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance = item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Updated SuccessFully!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})