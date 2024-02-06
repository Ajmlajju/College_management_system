from django.shortcuts import render,redirect
from admin_master.models import *
from django.http import JsonResponse
from admin_employee.models import *
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Employee, class_master, division_master, subjects, qualification_master, designation_master, department_master, employee_category_master, scd
import qrcode
from .models import department_employee
from .models import subjectclass
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.urls import reverse
# Create your views here.
def registration(request):
    i=''
    msg=''
    mesg=''
    empl=''
    if request.method == 'POST':
            empl_name = request.POST.get('emp_name')
            dofb = request.POST.get('dob')
            mobi = request.POST.get('mob')
            emai = request.POST.get('email')
            addr = request.POST.get('address')
            quali = request.POST.get('qual')
            quali_id = get_object_or_404(qualification_master, id=quali)
            desi = request.POST.get('des')
            desi_id = get_object_or_404(designation_master, id=desi)
            depa = request.POST.get('dep')
            depa_id = get_object_or_404(department_master, id=depa)
            empl_cat = request.POST.get('emp_cat')
            empl_cat_id = get_object_or_404(employee_category_master, id=empl_cat.split('+')[0])
            sala = request.POST.get('sal')
            jo_date = request.POST.get('j_date')
            photos = request.FILES.get('pic')
            gendr = request.POST.get('gender')

            qr_data = f"Name: {empl_name} \nDOB: {dofb}\nEmail:{emai} \nDepartment: {depa_id.name}\nJoin Date: {jo_date}"
            qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image to a BytesIO object
            qr_image_io = BytesIO()
            img.save(qr_image_io, format='PNG')
            qr_image_io.seek(0)

            # Create an InMemoryUploadedFile from BytesIO
            qr_image = InMemoryUploadedFile(
                file=qr_image_io,
                field_name=None,
                name=f'qr_code_{empl_name}_{emai}.png',
                content_type='image/png',
                size=qr_image_io.tell(),
                charset=None,
                )
            
            if Employee.objects.filter(emp_name=empl_name).exists():
                mesg="Name already exists. please enter with initial"
            if Employee.objects.filter(email=emai).exists():
                msg='Email exist.Enter a new email and try again.'
            else:
                empl = Employee(emp_name=empl_name, dob=dofb, mob=mobi, email=emai, address=addr,
                    qual_id=quali_id, des_id=desi_id, dept_id=depa_id, emp_cat_id=empl_cat_id,
                    salary=sala, j_date=jo_date, photo=photos, gender=gendr,barcode=qr_image)
                empl.save()
                
            dep= request.POST.get('dep')
            de_id = get_object_or_404(department_master, id=dep)
            frm_date = request.POST.get('j_date')
            # Validate and format the date
            frm_date_formatted = datetime.strptime(frm_date, '%Y-%m-%d').date()
            t_date=request.POST.get('')
            dep=department_employee(dept_id=de_id,from_date=frm_date_formatted,to_date=t_date,emp_id=empl)
            dep.save()

            des= request.POST.get('des')
            des_id = get_object_or_404(designation_master, id=des)
            frm_date = request.POST.get('j_date')
            # Validate and format the date
            fr_date_formatted = datetime.strptime(frm_date, '%Y-%m-%d').date()
            tdo_date=request.POST.get('')
            desig=designation_employee(des_id=des_id,emp_id=empl,from_date=fr_date_formatted,to_date=tdo_date)
            desig.save()

            salar= request.POST.get('sal')
            fram_date = request.POST.get('j_date')
            # Validate and format the date
            f_date_formatted = datetime.strptime(fram_date, '%Y-%m-%d').date()
            td_date=request.POST.get('')
            sal=emp_salary(emp_id=empl,salary=salar,from_date=f_date_formatted,to_date=td_date)
            sal.save()

            if empl_cat_id.area == 1:
                class_lst=request.POST.getlist('clas')
                sub_list=request.POST.getlist('divi')
                divi_list=request.POST.getlist('subj')
                if class_lst:
                    for i,j,k in zip(class_lst,sub_list,divi_list):
                        clss_id = get_object_or_404(class_master, id=i) 
                        divi_id = get_object_or_404(division_master, id=j)
                        subj_id = get_object_or_404(subjects, id=k)
                        scdi = scd(class_id=clss_id, div_id=divi_id, sub_id=subj_id, emp_id=empl)
                        scdi.save()

    clas = class_master.objects.all()
    div = division_master.objects.all()
    sub = subjects.objects.all()
    qua = qualification_master.objects.all()
    des = designation_master.objects.all()
    dep = department_master.objects.all()
    emp_category = employee_category_master.objects.all()
    context = {
        "clas": clas,
        "div": div,
        "sub": sub,
        'qua': qua,
        'des': des,
        'dep': dep,
        'emp': emp_category
    }
    return render(request, 'registration.html', {'mesg':mesg, 'msg': msg, **context})

def sublist(request):
    clsid = request.GET.get('id')
    subject_class_instances = subjectclass.objects.filter(classid=clsid).select_related('classid','subid')
    if subject_class_instances:
        data = [{
            'id': instance.subid.id,
            'subjectname': instance.subid.sname  # Include subjectname in the response
        } for instance in subject_class_instances]

        detailed_data = {
            'subjects': data,
        }
        return JsonResponse(detailed_data)
    else:
        return JsonResponse({'error': 'subject not found for given class'})
    
def emp_list(request):
    emp=Employee.objects.all()
    return render(request,'list_emp.html',{'emp':emp})

def edit_emp(request,id):
    msg = ''
    if request.method == 'POST':
        ename = request.POST.get('e_name')
        dofb = request.POST.get('dob')
        mobi = request.POST.get('mob')
        emai = request.POST.get('email')
        addr = request.POST.get('address')
        quali = request.POST.get('qual')
        q = qualification_master.objects.get(id=quali)
        jo_date = request.POST.get('j_date')
        photos = request.FILES.get('pic')
        if photos == '':
            p=request.POST['ph']
        else:
            p=request.FILES.get('pic')
        gendr = request.POST.get('gender')
        status = request.POST.get('sta')
        if Employee.objects.filter(email=emai).exclude(id=id).exists():
            msg = 'Email already exists'
        else:
            empl = Employee.objects.get(id=id)
            empl.emp_name = ename
            empl.dob = dofb
            empl.mob = mobi
            empl.email = emai
            empl.address = addr
            empl.qual_id = q
            empl.j_date = jo_date
            empl.photo = p
            empl.gender = gendr
            empl.status = status
            empl.save()
            return redirect('emplist')
    emp = Employee.objects.get(id=id)
    qua = qualification_master.objects.filter(status=1)
    return render(request, 'edit_emp.html', {'emp':emp,'qa':qua,'msg':msg})


def del_emp(request):
      em_id=request.GET['id']
      details=Employee.objects.get(id=em_id) 
      details.delete()
      return JsonResponse('deleted!!!') 

