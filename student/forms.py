from django import forms
from student.models import Student
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {"id":"user-password"}
        )
       
    )
    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        # TO-DO : attempts - invalid user min 25
        # if not qs.exists():
        #     raise forms.ValidationError({"username":"Invalid User Name"})
        return cleaned_data
    def __init__(self, *args, **kwargs):
        super(UserLoginForm  , self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field_name})


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
   
    # confriming the two passwords
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        username = cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError({"username":"Invalid User Name, Please Pick Another!"})
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            # error validation must be a dict with the field name as key and the error as value 
            raise forms.ValidationError({"password":"Passwords Fields Must Match!"})
        return cleaned_data

    # forgetting the args and kwargs causes mayham because the base form can't get the passed data from post requests
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field_name})


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        # use widget to override the original model in the displayed form
        widgets = {
            'password' : forms.PasswordInput(),
        }
        fields = ['firstName', 'lastName', 'mail']


    def __init__(self, *args, **kwargs):
        super(StudentModelForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field_name})

            
