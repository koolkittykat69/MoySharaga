from django.contrib import admin

# import models
from .models import University, Faculty, Department, Specialty, Group, Student, Teacher, Subject, Mark

class UniversityAdmin(admin.ModelAdmin):
    list_display = ("university_short_title", "university_title",)

class FacultyAdmin(admin.ModelAdmin):
    list_display = ("university", "faculty_short_title","faculty_title",)

admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department)
admin.site.register(Specialty)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)
