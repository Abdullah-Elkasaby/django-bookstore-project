from django import forms
from django.forms import fields
from admins.models import Employee
from django.contrib.auth import get_user_model

        
User = get_user_model()

class EmployeeModelForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ['firstName', 'lastName', 'mail', 'salary']


    def __init__(self, *args, **kwargs):
        super(EmployeeModelForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field_name})

