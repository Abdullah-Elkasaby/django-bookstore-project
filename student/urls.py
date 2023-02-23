from django.urls import path
from student.views import loginView, signupView, logoutView, editProfile, studentsView, searchStudent, viewStdProfile

urlpatterns = [
    
    path('login', loginView, name='login'),
    path('signup', signupView, name='signup'),
    path('logout', logoutView, name='logout'),
    path('editProfile', editProfile, name='editStudentProfile'),
    path('students', studentsView, name='studentsView'),
    path('search', searchStudent, name='searchStudent'),
    path('ownerofbook/<bookID>', viewStdProfile, name='ownedBy')

]