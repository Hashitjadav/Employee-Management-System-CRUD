from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            try:
                employee = Employee.objects.get(pk=id)
                form = EmployeeForm(instance=employee)
            except Employee.DoesNotExist:
                return redirect('/list')  # Redirect to the list if the employee does not exist
        return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            try:
                employee = Employee.objects.get(pk=id)
                form = EmployeeForm(request.POST, instance=employee)
            except Employee.DoesNotExist:
                return redirect('/list')  # Redirect to the list if the employee does not exist
        if form.is_valid():
            form.save()
        return redirect('/list')
    
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_list.html", context)

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
