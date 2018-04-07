from django.shortcuts import render, redirect
from books.models import BookItem
from .forms import BookItemForm

# Create your views here.

def booklist(request):
    book = BookItem.objects.all()
    return render(request, 'books/index.html', {'book':book})


def book_details(request, pk):
    book = BookItem.objects.get(pk=pk)
    return render(request, 'books/book_details.html', {'book':book})


def add_book(request):
    form = BookItemForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = BookItemForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
        # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return redirect('booklist')
        else:
        # The supplied form contained errors -
        # just print them to the terminal.
            print(form.errors)
        # Will handle the bad form, new form, or no form supplied cases.
        # Render the form with error messages (if any).
    return render(request, 'books/add_book.html', {'form': form})