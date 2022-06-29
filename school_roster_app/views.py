from django.shortcuts import render
from . models import School

from django.http import HttpResponse

my_school = School("Django School") 
# def home(request):
#     return HttpResponse('<h1>HOME</h1>')

def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    staff_data = {
        "staff_list": staff_list
    }
    return render(request, "pages/staff.html", staff_data)


def staff_detail(request, employee_id):
    pass # implement


def list_students(request):
    pass # implement


def student_detail(request, student_id):
    pass # implement    
