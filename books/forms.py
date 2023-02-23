from books.models import Book 
from django import forms

class BookModelForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ['name', 'price',  'img', 'category', 'onSale', 'description']
      
      
    def __init__(self, *args, **kwargs):
        super(BookModelForm  , self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field_name})
