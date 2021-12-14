from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee 

# Create your views here.
def index(request):
    context = {
        "employee_list":{}
    }
    return render(request, 'tables.html', context)

def show(request):
    tables = Employee.objects.all()
    context = {
        "employee_list":tables
    }
    return render(request, 'tables.html', context)

def search(request):
    print(request.GET["sql"])
    tables = Employee.objects.all()
    context = {
        "employee_list":tables
    }
    return render(request, 'tables.html', context)