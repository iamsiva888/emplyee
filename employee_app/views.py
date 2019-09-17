from django.shortcuts import render, redirect
from .models import Employee, Address, Number
from employee_app.forms import EmployeeForm, AddressFormset, NumberFormset


def home(request):
    return render(request, 'employee_app/home.html')


def employee_list(request):
    emp = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', {'emp': emp})


def employee_register(request):
    form1 = EmployeeForm(request.POST or None)
    form2 = AddressFormset(request.POST or None)
    form3 = NumberFormset(request.POST or None)

    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            user = form1.save(commit=False)
            user.save()

            address = form2.save(commit=False)
            for adres in address:
                adres.employee = user
                adres.save()

            number = form3.save(commit=False)
            for num in number:
                num.employee = user
                num.save()
            return redirect('employee_app:employee_list')
        else:
            return render(request, 'employee_app/employee_register.html', {'form1': form1, 'form2': form2, 'form3': form3})
    return render(request, 'employee_app/employee_register.html', {'form1': form1, 'form2': form2, 'form3': form3})


def employee_view(request, pk):
    emp = Employee.objects.get(pk=pk)
    addr = Address.objects.filter(employee=pk)
    nums = Number.objects.filter(employee=pk)

    return render(request, 'employee_app/employee_view.html', {'emp': emp, 'addr': addr, 'nums': nums})


def employee_edit(request, pk):
    name = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        form1 = EmployeeForm(request.POST, instance=name)
        form2 = AddressFormset(request.POST, instance=name)
        form3 = NumberFormset(request.POST, instance=name)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('employee_app:employee_list')
        else:
            return render(request, 'employee_app/employee_edit.html',
                          {'form1': form1, 'form2': form2, 'form3': form3})
    else:
        form1 = EmployeeForm(instance=name)
        form2 = AddressFormset(instance=name)
        form3 = NumberFormset(instance=name)
        return render(request, 'employee_app/employee_edit.html',
                      {'form1': form1, 'form2': form2, 'form3': form3})



def employee_delete_confirm(request, pk):
    emp = Employee.objects.get(pk=pk)
    return render(request, 'employee_app/employee_delete_confirm.html', {'emp': emp})


def employee_delete(request, pk):
    emp = Employee.objects.get(pk=pk)
    emp.delete()
    return redirect('employee_app:employee_list')
