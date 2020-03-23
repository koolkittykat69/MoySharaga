from django.urls import path

from . import views

app_name = 'panel'
urlpatterns = [

        path('', views.index, name = 'index'),
        path('student_id=<int:student_id>/', views.student, name = 'student'),
        path('timetable_id=<int:timetable_id>/', views.timetable, name = 'timetable'),

]
