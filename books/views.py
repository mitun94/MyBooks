from django.shortcuts import render
from books.models import BookItem

# Create your views here.

def booklist(request):
    book = BookItem.objects.all()
    return render(request, 'books/index.html', {'book':book})
