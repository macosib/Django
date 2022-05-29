from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    group = models.CharField(max_length=10, verbose_name='Класс')
    teacher = models.ManyToManyField(Teacher, related_name='students')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name
