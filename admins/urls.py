from django.urls import path
from admins.views import CreateAdminView, editProfile


urlpatterns = [
    path('create', CreateAdminView, name='adminSignup'),
    path('editprofile', editProfile, name='editAdminProfile'),
]