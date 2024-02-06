from django.db import models

# Create your models here.

class department_master(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=30)
    status=models.IntegerField(default=1)

class designation_master(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=30)
    status=models.IntegerField(default=1)

class qualification_master(models.Model):
    name=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class class_master(models.Model):
    name=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class division_master(models.Model):
    name=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class employee_category_master(models.Model):
    EMPLOYEE_CATEGORY_CHOICES=[
        (1,'Teacher'),
        (2,'Librarian'),
        (3,'cafeteria'),
        (4,'Accountant'),
        (5,'Others')
    ]
    name=models.CharField(max_length=100)
    area=models.IntegerField(choices=EMPLOYEE_CATEGORY_CHOICES)
    status=models.IntegerField(default=1)

class subjects(models.Model):
    sname=models.CharField(max_length=100)
    sstatus=models.BooleanField(default=1)

class subjectclass(models.Model):
    classid=models.ForeignKey("class_master",on_delete=models.CASCADE)
    subid=models.ForeignKey("subjects",on_delete=models.CASCADE)