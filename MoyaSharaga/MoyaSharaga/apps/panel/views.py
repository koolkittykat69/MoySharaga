from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import University, Student, Group 

def home_view(request):
    return render(request, 'base.html')

def index(request):
    university_list = University.objects.all()
    return render(request, 'search.html', {'university_list': university_list})

def student(request, student_id):
    try:
        student = Student.objects.get(id = student_id)
    except:
        raise Http404("Студент не найден")
    return render(request, 'student.html', {'student': student})

