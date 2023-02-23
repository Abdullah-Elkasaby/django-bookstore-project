from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from books.models import Book

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mail = models.CharField(unique=True, max_length=150)
    salary = models.DecimalField( decimal_places=2, max_digits=7, default=5000)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name='addedBy')
    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.mail}"

    