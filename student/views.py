from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from student.forms import UserRegisterForm, UserLoginForm, StudentModelForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from student.models import Student
from books.models import Book

User = get_user_model()

# Create your views here.

def loginView(request):
    form = UserLoginForm(request.POST or None)
    if not request.user.username and "home" in request.META.get('HTTP_REFERER'):
        messages.info(request, "You Must Be Logged In To Check Books!")
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password )
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials!")
    return  render(request, 'student/login.html', {"form":form})

def signupView(request):
    # paraentheses to use an instance of the class
    userform = UserRegisterForm(request.POST or None)
    studentform = StudentModelForm(request.POST or None)

    if userform.is_valid() and studentform.is_valid():
        username = userform.cleaned_data.get('username')
        password = userform.cleaned_data.get('password')
        # saveing student as an object but not in database to be able to add it to user
        student = studentform.save(commit=False)
        user = User.objects.create_user(username=username, password=password)
        user.first_name = student.firstName
        user.last_name =student.lastName
        student.user = user
        student.username = username
        user.save()
        student.save()
        messages.success(request, f"Account Created For {username} Successfuly!")

    return render(request, 'student/signup.html', {'form': userform, "studentform": studentform})

@login_required(login_url='login')
def editProfile(request):
    user = request.user
    student = user.student    
    prev_student = {"firstName":student.firstName, "lastName": student.lastName, "mail": student.mail}
    # initial adds a default value to html
    userform = UserRegisterForm(request.POST or None, initial={"username":user.username})
    studentform = StudentModelForm(request.POST or None, initial = prev_student)
    # SEARCH FOR A BETTER WAY TO A UPDATE IT
    if userform.is_valid() and studentform.is_valid():
        user.username = userform.cleaned_data.get('username') 
        user.set_password(userform.cleaned_data.get('password')) 
        user.first_name = studentform.cleaned_data.get('firstName')
        user.last_name = studentform.cleaned_data.get('lastName')
        student.username= userform.cleaned_data.get('username')
        student.lastName = studentform.cleaned_data.get('lastName')
        student.firstName = studentform.cleaned_data.get('firstName')
        student.mail = studentform.cleaned_data.get('mail')
        user.save()
        student.save()
        messages.success(request, f"Account Info For {user.username} Edited Successfuly!")    
    return render(request, 'student/editprofile.html', {'form': userform, "studentform": studentform})

def logoutView(request):
    logout(request)
    return redirect('login')

staff_member_required(login_url='login')
def studentsView(request):
    if request.user.is_staff:
        students = Student.objects.all()
        return render(request, 'student/students.html', {"students":students})


staff_member_required(login_url='login')
def searchStudent(request):
    std_id = int (request.POST['search_word'])
    std = get_list_or_404(Student, pk=std_id)
    if request.user.is_staff:
        return render(request, 'student/students.html', {"students": std})


staff_member_required(login_url='login')
def viewStdProfile(request, bookID):
    book = Book.objects.get(pk=bookID)
    stds = book.ownedBy.all()
    if request.user.is_staff:
        return render(request, 'student/students.html', {"students": stds})

