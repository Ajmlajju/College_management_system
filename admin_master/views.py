from django.shortcuts import render,redirect,get_object_or_404
from admin_master.models import *
from django.http import JsonResponse
from django.conf import settings
# Create your views here.

def admin_master_department(request):
    message=''
    msg=''
    if request.method=='POST':
        name=request.POST['dept_name'].strip()
        code=request.POST['dept_code'].strip()
        if not name or not code: 
               message="name and code are required"   
        elif department_master.objects.filter(name=name).exists():
               message="name already exists"
        elif department_master.objects.filter(code=code).exists():
               message="code already exists"
        else:
              ins=department_master(name=name,code=code)
              ins.save()
              msg="Successfully inserted"
    display=department_master.objects.all()
    return render(request,'admin_master_department_manage.html',{'msg':message,'mseg':msg,'display':display}) 

def datapick_edit(request):
       responsedata=department_master.objects.get(id=request.GET['id'])
       serialized_data={
              'name':responsedata.name,
              'code':responsedata.code,
              'status':responsedata.status,
       }
       return JsonResponse(serialized_data)

def update_dept_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_code = request.GET['updateCode'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name or not update_code:
            error_message = 'Department name and code are required.'
    else:
        if department_master.objects.exclude(id=update_id).filter(name__iexact=update_name).exists():
            error_message = 'Department name already exists.'
        elif department_master.objects.exclude(id=update_id).filter(code__iexact=update_code).exists():
            error_message = 'Department code already exists.'
        else:
            obj= department_master.objects.get(id=update_id)
            obj.name = update_name
            obj.code = update_code
            obj.status=int(update_Status)
            obj.save()
            success_message = 'Department updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  
def del_depart(request):
      dept_id=request.GET['id']
      details=department_master.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!')    


def admin_master_designation(request):
    msg=''
    mesg=''
    if request.method=='POST':
            name=request.POST['desig_name'].strip()
            code=request.POST['desig_code'].strip()
            if not name or not code:
                msg="code and name are required"
            elif designation_master.objects.filter(name=name).exists():
               message="name already exists"
            elif designation_master.objects.filter(code=code).exists():
               message="code already exists"
            else:
                 ins=designation_master(name=name,code=code)
                 ins.save()
                 mesg="successfully inserted"
    display=designation_master.objects.all()
    return render(request,'admin_master_designation_manage.html',{'display':display,"msg":msg,'mesg':mesg})


def datapick_desig_edit(request):
       responsedata=designation_master.objects.get(id=request.GET['id'])
       serialized_data={
              'name':responsedata.name,
              'code':responsedata.code,
              'status':responsedata.status,
       }
       return JsonResponse(serialized_data)

def update_desig_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_code = request.GET['updateCode'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name or not update_code:
            error_message = 'Designation name and code are required.'
    else:
        if designation_master.objects.exclude(id=update_id).filter(name__iexact=update_name).exists():
            error_message = 'Designation name already exists.'
        elif designation_master.objects.exclude(id=update_id).filter(code__iexact=update_code).exists():
            error_message = 'Code already exists.'
        else:
            obj= designation_master.objects.get(id=update_id)
            obj.name = update_name
            obj.code = update_code
            obj.status=int(update_Status)
            obj.save()
            success_message = 'Designation updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  
def del_desig(request):
      dept_id=request.GET['id']
      details=designation_master.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!')    

def admin_master_qualification(request):
    message=''
    msg=''
    if request.method=='POST':
        name=request.POST['qual_name'].strip()
        if not name: 
               message="name required"   
        elif qualification_master.objects.filter(name=name).exists():
               message="name already exists"
        else:
              ins=qualification_master(name=name)
              ins.save()
              msg="Successfully inserted"
    display=qualification_master.objects.all()
    return render(request,'admin_master_qualification_manage.html',{'msg':message,'mseg':msg,'display':display}) 

def datapick_qualif_edit(request):
       responsedata=qualification_master.objects.get(id=request.GET['id'])
       serialized_data={
              'name':responsedata.name,
              'status':responsedata.status,
       }
       return JsonResponse(serialized_data)

def update_qualif_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name:
            error_message = 'Qualification name and code are required.'
    else:
        if qualification_master.objects.exclude(id=update_id).filter(name__iexact=update_name).exists():
            error_message = 'Qualification name already exists.'
        else:
            obj= qualification_master.objects.get(id=update_id)
            obj.name = update_name
            obj.status=int(update_Status)
            obj.save()
            success_message = 'Qualification updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  
def del_qualif(request):
      dept_id=request.GET['id']
      details=qualification_master.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!')    

def admin_master_class(request):
    message=''
    msg=''
    if request.method=='POST':
        name=request.POST['class_name'].strip()
        if not name: 
               message="name required"   
        elif class_master.objects.filter(name=name).exists():
               message="name already exists"
        else:
              ins=class_master(name=name)
              ins.save()
              msg="Successfully inserted"
    display=class_master.objects.all()
    return render(request,'admin_master_class_manage.html',{'msg':message,'mseg':msg,'display':display}) 

def datapick_class_edit(request):
       responsedata=class_master.objects.get(id=request.GET['id'])
       serialized_data={
              'name':responsedata.name,
              'status':responsedata.status,
       }
       return JsonResponse(serialized_data)

def update_class_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name:
            error_message = 'class name required.'
    else:
        if class_master.objects.exclude(id=update_id).filter(name__iexact=update_name).exists():
            error_message = 'class name already exists.'
        else:
            obj= class_master.objects.get(id=update_id)
            obj.name = update_name
            obj.status=int(update_Status)
            obj.save()
            success_message = 'Class updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  
def del_class(request):
      dept_id=request.GET['id']
      details=class_master.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!') 


def admin_master_division(request):
    message=''
    msg=''
    if request.method=='POST':
        name=request.POST['division_name'].strip()
        if not name: 
               message="name required"   
        elif division_master.objects.filter(name=name).exists():
               message="division already exists"
        else:
              ins=division_master(name=name)
              ins.save()
              msg="Successfully inserted"
    display=division_master.objects.all()
    return render(request,'admin_master_division_manage.html',{'msg':message,'mseg':msg,'display':display}) 

def datapick_division_edit(request):
       responsedata=division_master.objects.get(id=request.GET['id'])
       serialized_data={
              'name':responsedata.name,
              'status':responsedata.status,
       }
       return JsonResponse(serialized_data)

def update_division_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name:
            error_message = 'division name required.'
    else:
        if division_master.objects.exclude(id=update_id).filter(name__iexact=update_name).exists():
            error_message = 'Division name already exists.'

        else:
            obj= division_master.objects.get(id=update_id)
            obj.name = update_name
            obj.status=int(update_Status)
            obj.save()
            success_message = 'Division updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  
def del_division(request):
      dept_id=request.GET['id']
      details=division_master.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!') 

def admin_master_employee_category(request):
    message=''
    msg=''
    if request.method=='POST':
        name=request.POST['emp_cat_name'].strip()
        area=request.POST['area'].strip()
        if not name or not area: 
               message="name and code are required"   
        elif employee_category_master.objects.filter(name=name).exists():
               message="name already exists"
        elif employee_category_master.objects.exclude(area=settings.EMPLOYEE_CATEGORY_AREA_OTHERS).filter(area=area).exists():
               message="area already exists"
        else:
              ins=employee_category_master(name=name,area=area)
              ins.save()
              msg="Successfully inserted"
    display=employee_category_master.objects.all()
    return render(request,'admin_master_employee_category_manage.html',{'msg':message,'mseg':msg,'display':display,'settings':settings}) 

def datapick_edit_employee(request):
       responsedata=employee_category_master.objects.get(id=request.GET['id'])
       serialized_data={
              'name':responsedata.name,
              'area':responsedata.area,
              'status':responsedata.status,
       }
       return JsonResponse(serialized_data)

def update_emp_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_code = request.GET['updateCode'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name or not update_code:
            error_message='Employee category name and code are required.'
    else:
        if employee_category_master.objects.exclude(id=update_id).filter(name=update_name).exists():
            error_message='Employee category name already exists.'
        elif employee_category_master.objects.exclude(id=update_id).filter(area=update_code).exists():
            error_message='Employee category code already exists.'
        else:
            obj= employee_category_master.objects.get(id=update_id)
            obj.name=update_name
            obj.area=update_code
            obj.status=int(update_Status)
            obj.save()
            success_message='Department updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  
def del_emp(request):
      dept_id=request.GET['id']
      details=employee_category_master.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!') 

def subject(request):
     success=""
     failed=""
     if request.method=='POST':
          all=request.POST.getlist('checkitems')
          name=request.POST['sname'].strip()
          if not name:
               failed="subject name required"
          else:
               if subjects.objects.filter(sname=name).exists():
                    failed="subject already exists"
                
               else:
                    subforeign,foreign=subjects.objects.get_or_create(sname=name)
                    for clas in all:
                         get= get_object_or_404(class_master,pk=int(clas))
                         obj=subjectclass(classid=get,subid=subforeign)
                         obj.save()
                         success="submitted"    
     a=class_master.objects.all().values    
     b=subjects.objects.all().values
     return render(request,'admin_master_subject_manage.html',{'class':a,'subjects':b,'mesg':success,'msg':failed})
 
def datapick_edit_sub(request):
       id=request.GET['id']
       responsedata=subjects.objects.get(id=id)
       alldata=subjectclass.objects.filter(subid=id).values_list('classid__name',flat=True)
       serialized_data={
              'name':responsedata.sname,
              'class_data':list(alldata),
              'status': 1 if responsedata.sstatus else 0,
       }
       return JsonResponse(serialized_data)

def update_sub_details(request):
  if request.method == 'GET':
    update_id = request.GET['updateId']
    update_name = request.GET['updateName'].strip()
    update_Status = request.GET['updateStatus']
    error_message=None
    success_message=None
    if not update_name:
            error_message='subject name required.'
    else:
        if subjects.objects.exclude(id=update_id).filter(sname=update_name).exists():
            error_message='Subject name already exists.'
        else:
            obj= subjects.objects.get(id=update_id)
            obj.sname=update_name
            obj.sstatus=int(update_Status)
            obj.save()
            success_message='Subjects updated successfully.'
    response_data = {
    'errormessage': error_message,
    'successmessage': success_message,
    }
    return JsonResponse(response_data)
  

def del_sub(request):
      dept_id=request.GET['id']
      details=subjects.objects.get(id=dept_id) 
      details.delete()
      return JsonResponse('deleted!!!') 


