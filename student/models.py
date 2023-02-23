from django.db import models
from books.models import Book
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, editable=False)
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mail = models.EmailField(unique=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name='ownedBy')
    readonly_fields = ["username"]
    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.mail}"
