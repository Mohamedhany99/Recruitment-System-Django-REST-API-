from django.shortcuts import render
from hr_management.models import Employee 
# Create your views here.
def index(request):
    context = {
        'Employee': Employee.objects.all(),
    }
    return render(request, 'index.html', context)
