from django import forms
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from admins.forms import EmployeeModelForm
from books.models import Book
from student.forms import UserRegisterForm
from django.contrib.admin.views.decorators import staff_member_required 
User = get_user_model()
# Create your views here.

staff_member_required(login_url=('login'))
def CreateAdminView(request):
    adminform = UserRegisterForm(request.POST or None)
    empform = EmployeeModelForm(request.POST or None)
    if adminform.is_valid() and empform.is_valid():
        username = adminform.cleaned_data.get('username')
        password = adminform.cleaned_data.get('password')
        user = User.objects.create_superuser(username=username, password=password)
        employee = empform.save(commit=False)
        employee.username = username
        user.first_name = employee.firstName
        user.last_name =employee.lastName
        employee.user = user
        employee.save()
        user.save()
        messages.success(request, f"Account Created For Admin {username} Successfuly!")

    return render(request, "admins/signup.html", {"adminform":adminform, "empform":empform})

@staff_member_required(login_url='login')
def editProfile(request):
    user = request.user
    emp = user.employee    
    prev_emp = {"firstName":emp.firstName, "lastName": emp.lastName, "mail": emp.mail}
    # initial adds a default value to html
    userform = UserRegisterForm(request.POST or None, initial={"username":user.username})
    empform = EmployeeModelForm(request.POST or None, initial = prev_emp)
    # Admin can't edit own salary
    empform.fields.get('salary').widget = forms.HiddenInput()
    # SEARCH FOR A BETTER WAY TO A UPDATE IT
    if userform.is_valid() and empform.is_valid():
        user.username = userform.cleaned_data.get('username') 
        user.set_password(userform.cleaned_data.get('password')) 
        user.first_name = empform.cleaned_data.get('firstName')
        user.last_name = empform.cleaned_data.get('lastName')
        emp.username= userform.cleaned_data.get('username')
        emp.lastName = empform.cleaned_data.get('lastName')
        emp.firstName = empform.cleaned_data.get('firstName')
        emp.mail = empform.cleaned_data.get('mail')
        user.save()
        emp.save()
        messages.success(request, f"Account Info For {user.username} Edited Successfuly!")    
    return render(request, "admins/editprofile.html", {"adminform": userform, "empform": empform})


