# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    data = {'first_name': 'Vivek', 'last_name': 'Rajyaguru'}
    return render(request, 'about.html', data)