from django.shortcuts import render, get_object_or_404
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

from django.views.generic.detail import DetailView

# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
