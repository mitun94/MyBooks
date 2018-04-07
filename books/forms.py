from django import forms
from .models import BookItem,Category

class BookItemForm(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = ('title','author','category','description')