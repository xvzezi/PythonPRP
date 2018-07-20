# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

class DataModel(models.Model):
    student_ID = models.CharField(max_length = 12)
    name = models.CharField(max_length = 30)
    department = models.CharField(max_length = 20)
    major = models.CharField(max_length = 20)
    grade = models.IntegerField()
    graduate_time = models.CharField(max_length = 10)
    student_status = models.CharField(max_length = 4)
    failed_number = models.IntegerField()
    center_credits = models.IntegerField()
    courses_must_to_take = models.CharField(max_length = 400)
    a_group = models.CharField(max_length = 5)
    b_group = models.CharField(max_length = 5)
    c_group = models.CharField(max_length = 5)
    d_group = models.CharField(max_length = 5)
    professional_elective_courses = models.CharField(max_length = 5)
    enterprise_education_courses = models.CharField(max_length = 5)
    general_courses = models.CharField(max_length = 50)
    others = models.CharField(max_length = 1000)

class UserLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())