from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import TimetableForm
from .models import University, Student, Group, Timetable

def home_view(request):
    return render(request, 'base.html')

def index(request, student_id):
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

def timetable(request, timetable_id):
    try:
        timetable = Timetable.objects.get(id = timetable_id)
    except:
        raise Http404("Расписание не найдено")
    return render(request, 'timetable.html', {'timetable': timetable})

def time_new(request):
    if request.method == "POST":
        form = TimetableForm(request.POST)
        if form.is_valid():
            timetable = form.save()
            timetable.save()
            return render(request, 'time_new.html', {'form': form})
    else:
        form = TimetableForm()
        return render(request, 'time_new.html', {'form': form})
