from django import forms
from django.forms import inlineformset_factory

from .models import Employee, Address, Number


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name', 'required':'True'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['des', 'employee']

        widgets = {
            'des': forms.Textarea(attrs={'cols': 50, 'rows': 3, 'class': 'form-control', 'placeholder': 'Enter Address', 'required':'True'}),
        }


AddressFormset = inlineformset_factory(Employee, Address, form=AddressForm, extra=0, min_num=1, max_num=3, )


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['num', 'employee']
        widgets = {
            'num': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number', 'required':'True'}),
        }


NumberFormset = inlineformset_factory(Employee, Number, form=NumberForm, extra=0, min_num=1, max_num=3, )
