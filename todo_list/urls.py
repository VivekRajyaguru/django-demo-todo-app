"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url('about/', views.about, name='about'),
    url('delete/(?P<list_id>.*)', views.delete, name='delete'),
    url('edit/(?P<list_id>.*)', views.edit, name='edit'),
    url('updatestatus/(?P<list_id>.*)/(?P<flag>.*)', views.updatestatus, name='updatestatus'),
    url('', views.home, name='home'),
    
]
