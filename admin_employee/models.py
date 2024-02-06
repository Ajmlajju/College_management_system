from django.db import models
from admin_master.models import *
# Create your models here.

class Employee(models.Model):
    emp_cat_id= models.ForeignKey(employee_category_master,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=255)
    dob = models.DateField()
    mob = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.TextField()
    j_date = models.DateField()
    dept_id= models.ForeignKey(department_master,on_delete=models.CASCADE)
    des_id= models.ForeignKey(designation_master,on_delete=models.CASCADE)
    qual_id= models.ForeignKey(qualification_master,on_delete=models.CASCADE)
    salary=models.DecimalField(max_digits=100,decimal_places=2)
    GENDER_CHOICES=[
         (1,'male'),
         (2,'female'),
         (3,'others')
    ]
    gender=models.IntegerField(choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    barcode=models.ImageField(upload_to='barcode/',blank=True, null=True)
    status=models.IntegerField(default=1)

    def delete(self, *args, **kwargs):
        # Delete the barcode file
        if self.barcode:
            self.barcode.delete(save=False)
        # Delete the photo file
        if self.photo:
            self.photo.delete(save=False)
        super().delete(*args, **kwargs)

class scd(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    class_id=models.ForeignKey(class_master,on_delete=models.CASCADE)
    div_id= models.ForeignKey(division_master,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(subjects,on_delete=models.CASCADE)

class department_employee(models.Model):
     dept_id= models.ForeignKey(department_master,on_delete=models.CASCADE)
     emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
     from_date=models.DateField()
     to_date=models.DateField(null=True, blank=True)

class designation_employee(models.Model):
     des_id= models.ForeignKey(designation_master,on_delete=models.CASCADE)
     emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
     from_date=models.DateField()
     to_date=models.DateField(null=True, blank=True)

class emp_salary(models.Model):
     emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
     salary=models.DecimalField(max_digits=100,decimal_places=2)
     from_date=models.DateField()
     to_date=models.DateField(null=True, blank=True)

     



