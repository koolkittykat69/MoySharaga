from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import University

def index(request):
	university_list = University.objects.all()
	return render(request, 'panel/list.html', {'university_list': university_list})
# Create your views here.

