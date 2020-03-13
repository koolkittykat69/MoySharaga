from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import University

def home_view(request):
    return render(request, 'base.html')

def index(request):
    university_list = University.objects.all()
    return render(request, 'search.html', {'university_list': university_list})

