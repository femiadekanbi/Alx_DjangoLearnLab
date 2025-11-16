from bookshelf.models import Book

# Retrieve all books
all_books = Book.objects.all()
print(all_books)  # <QuerySet [<Book: 1984 by George Orwell (1949)>, ...]>

# Retrieve a single book by title
book_1984 = Book.objects.get(title="1984")
print(book_1984)  # <Book: 1984 by George Orwell (1949)>

# Filter books published after 2000
recent_books = Book.objects.filter(publication_year__gt=2000)
print(recent_books)  # <QuerySet [<Book: Example Book (2010)>, ...]>
