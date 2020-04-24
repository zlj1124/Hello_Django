# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Grade(models.Model):
    g_name=models.CharField(max_length=32,db_column="grade",default='')

    class Meta:
        db_table = "grade"
        verbose_name = u'班级'
        verbose_name_plural = verbose_name

class Student(models.Model):
    s_name=models.CharField(max_length=32,db_column="name",default='')
    s_grade =models.ForeignKey(Grade) 

    @classmethod
    def crate(cls,s_name,s_grade=1):
        return cls(s_name=s_name,s_grade=s_grade)

    class Meta:
        db_table = 'student'
        verbose_name = u'学生'
        verbose_name_plural = verbose_name

class Teacher(models.Model):
    t_name = models.CharField(max_length=32,null=True)
    t_grade = models.ManyToManyField('Grade',null=True)  

    class Meta:
        db_table = 'teacher'
        verbose_name = u'老师'
        verbose_name_plural = verbose_name