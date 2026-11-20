from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def home(request):

    employees = employees.objects.all()
    return render(request,'employee/home.html',{'employees':employees})

def add_employee(request):

    if request.method == "POST":
        form = EmployeeForm(request.form)

        if  form.is_valid():
            form.save()
            return redirect('home.html')

        else:
            form=EmployeeForm()
            return render(request,'employee/add_employee.html', {'form':form})

def update_employee(request,id):

    employee= get_object_or_404(Employee,id)

    if request.method == 'POST':
        form=EmployeeForm(request.POST,instance=employee)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:

            form=EmployeeForm(instance=employee)
            return render(request,'employee/update_employee.html',{'form':form})

def delete_employee(request,id):

    employee=get_object_or_404(Employee,id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request,'employee/delete_employee.html',{'employee':employee})






            
        



       



