from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'group']
    ordering = ['group']
    filter_horizontal = ['teacher']
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'subject']
    ordering = ['name']
