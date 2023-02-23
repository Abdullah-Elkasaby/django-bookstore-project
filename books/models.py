from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    book_choices = (
        ('t', 'Available'),
        ('f', 'Borrowed')
    )
    status = models.CharField(max_length=15, choices=book_choices, default='t')
    description = models.TextField(max_length=500, null=True)
    img = models.CharField(max_length=100 ,null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='books')
    return_date = models.DateField(null=True)
    onSale = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.category}"
