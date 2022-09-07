from concurrent.futures import process
from multiprocessing import context
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render ,redirect ,get_object_or_404,HttpResponse
from .models import Projects, Staff, Major_skills
from django.contrib.auth.models import User


#0.00 Login page:
def login_admin(request):
    if request.user.is_authenticated:
        return redirect('home_set')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'This is not a user')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home_set')
        else:
            return HttpResponse('You are not allowed')

    return render(request,'login.html')

#0.10 Login page:

def logout_admin(request):
    logout(request)
    return redirect('login')




#---------------------------------------------------------------------------------------|>

#1.00 Projects page:
@login_required(login_url='login')
def projects_page(request):
    projects =Projects.objects.order_by('id')
    return render(request,'Projects_Page.html',{'projects':projects})

#1.10 To check project completenss:
@login_required(login_url='login')
def projects_complete(request,id):
    complete = Projects.objects.get(pk = id)
    complete.complete = True
    complete.save()
    return redirect('home_set')

#1.20 To add new project:
@login_required(login_url='login')
def adding_project(request):
    user=User.objects.first()
    if request.method == 'POST':
        completeness = request.POST.get('complete')
        print(completeness)
        if completeness=='status':
            is_complete = True
            Projects.objects.create(
            agix_manager = user,
            project_name = request.POST['project_name'],
            client_name = request.POST['client_name'],
            project_description = request.POST['description'],
            project_image = request.FILES.get('pic'),
            complete = is_complete,
            )
            return redirect('home_set')
            # print(True)
        else:
            is_complete = False
            # print(False)
            Projects.objects.create(
            agix_manager = user,
            project_name = request.POST['project_name'],
            client_name = request.POST['client_name'],
            project_description = request.POST['description'],
            project_image = request.FILES.get('pic'),
            complete = is_complete,
            )
            return redirect('home_set')
        
        

    return render(request,'adding_projects.html')


#1.30 To update projects

@login_required(login_url='login')
def update_project(request,up_id):
    user=User.objects.first()
    upated_project = Projects.objects.get(pk=up_id)
    
    if request.method == 'POST':
        completeness = request.POST.get('complete')
        print(completeness)
        if completeness=='status':
            is_complete = True
            upated_project.agix_manager = user,
            upated_project.project_name = request.POST['project_name']
            upated_project.client_name = request.POST['client_name']
            upated_project.project_description = request.POST['description']
            upated_project.project_image = request.FILES.get('pic')
            upated_project.complete = is_complete
            upated_project.save()

            return redirect('home_set')
        
        else:
            is_complete = False
            # print(False)
            upated_project.project_name = request.POST['project_name']
            upated_project.client_name = request.POST['client_name'],
            upated_project.project_description = request.POST['description']
            upated_project.project_image = request.FILES.get('pic')
            upated_project.complete = is_complete
            upated_project.save()

            return redirect('home_set')
        

    return render(request,'adding_projects.html')

#1.40 delete projects

@login_required(login_url='login')
def delete_project(request,dl_id):
    deleted_project = Projects.objects.get(pk=dl_id)
    deleted_project.delete()
    return redirect('home_set')

def project_details(request,id_num):
    project = get_object_or_404(Projects,pk=id_num)
    return render(request,'projects_details.html',{'project':project})

#1.50 To delete all projects

def deleteAll(request):
    allItems = Projects.objects.all()
    allItems.delete()

    return redirect('home_set')

#-------------------------------------------------------------------------------------------|>


#2.00 Staff Page

#2.10 Company staff data
@login_required(login_url='login')
def staff(request):
    staff = Staff.objects.order_by('id')
    return render(request,'Staff.html',{'staff':staff})

#2.2 Staff personal data

def personal(request,prf_id):
    pers_profile = Staff.objects.get(pk=prf_id)
    employee_job = pers_profile.major_skills_set.all()
    previous_participants=pers_profile.employee_previous_project.all()

    return render(request,'staff_profile.html',{'pers_profile':pers_profile,'employee_job':employee_job,'previous_participants':previous_participants})

#2.3 To add new Staff 


def adding_employee(request):
    projects =Projects.objects.all()
    skills =['ETABS','SAFE','MIDAS GEN','ROBOT',
    'PROKON','SAP2000','STAAD PRO','MICROSOFT OFFICE',
    'MICROSOT WORD','AUTOCAD','REVIT','3D MAX','LUMIA']
    if request.method =='POST':
        professional_skills=request.POST.getlist('skill')
        work_participations = request.POST.getlist('proj')
        
        Staff.objects.create(
            employee_name=request.POST['employee_name'],
            employee_major=request.POST['major'],
            employee_description=request.POST['description'],
            employee_profile_picture =request.FILES.get('ps')
        )

        for i in work_participations:
            p= Projects.objects.get(project_name=i)
            se=Staff.objects.get(employee_name=request.POST['employee_name'])
            se.employee_previous_project.add(p)
            se.save()
        se
               
        for skill in professional_skills:
            Major_skills.objects.create(
            employee = se,
            skills = skill)
       

        return redirect('staff')


    context={'projects':projects,'skills':skills}
    return render(request,'adding_employee.html',context)

#2.4 To update existing Staff 

def update_employee(request,up_id):
    updated_employee=Staff.objects.get(pk = up_id)
    projects =Projects.objects.all()
    skills =['ETABS','SAFE','MIDAS GEN','ROBOT',
    'PROKON','SAP2000','STAAD PRO','MICROSOFT OFFICE',
    'MICROSOT WORD','AUTOCAD','REVIT','3D MAX','LUMIA']
    

    if request.method =='POST':
        professional_skills=request.POST.getlist('skill')
        work_participations = request.POST.getlist('proj')

        
        updated_employee.employee_name=request.POST['employee_name']
        updated_employee.employee_major=request.POST['major']
        updated_employee.employee_description=request.POST['description']
        updated_employee.employee_profile_picture =request.FILES.get('ps')
        updated_employee.save()

        
        
        for i in work_participations:
            p= Projects.objects.get(project_name=i)
            se=updated_employee
            se.employee_previous_project.add(p)
            se.save()

        updated_employee.major_skills_set.all().delete()

        for skill in professional_skills:
            Major_skills.objects.create(employee = updated_employee,  
            skills = skill)
        
       

        return redirect('staff')

    context={'projects':projects,'skills':skills}
    return render(request,'adding_employee.html',context)

#2.5 To update existing Staff 

def delete_employee(request,dl_id):
    deleted_employee = Staff.objects.get(pk = dl_id)
    deleted_employee.delete()
    return redirect('staff')

#-------------------------------------------------------------------------------------------|>

                                #   The Project End.