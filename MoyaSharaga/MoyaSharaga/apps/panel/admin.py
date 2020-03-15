from django.contrib import admin

# import models
from .models import University, Faculty, Department, Specialty, Group, Student, Teacher, Subject, Mark

class UniversityAdmin(admin.ModelAdmin):
    list_display = ("university_short_title", "university_title")

class FacultyAdmin(admin.ModelAdmin):
    list_display = ("faculty_short_title", "faculty_title", "university")

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_short_title", "department_title", "faculty")

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("specialty_title", "department")

class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_title", "specialty")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_surname", "student_name", "student_patronymic", "group")


admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)
