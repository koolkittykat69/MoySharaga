from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import University, Student, Group 

def home_view(request):
    return render(request, 'base.html')

def index(request):
    if request.GET.get("search"):
        search = request.GET.get("search")
        students_search = Student.objects.filter(student_surname = search)
        return render(request, 'results.html', {'students_search': students_search})
    else:
        return render(request, 'search.html')

def student(request, student_id):
    try:
        student = Student.objects.get(id = student_id)
    except:
        raise Http404("Студент не найден")
    return render(request, 'student.html', {'student': student})

