from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from relationship_app.models import Book, Library  # <-- use full app path

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
