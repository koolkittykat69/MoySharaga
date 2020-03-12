from django.contrib import admin

# import models
from .models import University, Faculty, Department, Specialty, Student, Teacher

# creating model's registration for admin panel
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Specialty)
admin.site.register(Student)
admin.site.register(Teacher)
