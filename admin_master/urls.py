"""
URL configuration for ams project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('admin_master_department',admin_master_department,name='master_department'),
    path('admin_master_designation',admin_master_designation,name='master_designation'),
    path('admin_master_qualification',admin_master_qualification,name='master_qualification'),
    path('admin_master_class',admin_master_class,name='master_class'),
    path('admin_master_division',admin_master_division,name='master_division'),
    path('admin_master_employee_category',admin_master_employee_category,name='master_employee'),
    path('edit_department/',datapick_edit,name="data"),
    path('update_depart/',update_dept_details,name="update_depart"),
    path('delete_depart/',del_depart,name='del_depart'),
    path('edit_designation/',datapick_desig_edit,name="datadesig"),
    path('update_desig/',update_desig_details),
    path('delete_desig/',del_desig,name='del_desig'),
    path('edit_qualification/',datapick_qualif_edit),
    path('update_qualification/',update_qualif_details),
    path('delete_qualif/',del_qualif),
    path('edit_class/',datapick_class_edit),
    path('update_class/',update_class_details),
    path('delete_class/',del_class),
    path('edit_division/',datapick_division_edit),
    path('update_division/',update_division_details),
    path('delete_division/',del_division),
    path('edit_emp/',datapick_edit_employee),
    path('update_emp/',update_emp_details),
    path('delete_emp/',del_emp),
    path('subject_page',subject,name="sub"),
    path('edit_sub/',datapick_edit_sub),
    path('update_sub/',update_sub_details), 
    path('del_sub/',del_sub)
]
