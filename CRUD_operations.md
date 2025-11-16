# CRUD Operations for Book Model

## 1. Import Model
```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
book

<Book: 1984 by George Orwell (1949)>

Book.objects.all()

<QuerySet [<Book: 1984 by George Orwell (1949)>]>

Book.objects.get(id=1)

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book

book = Book.objects.get(id=1)
book.delete()

(1, {'bookshelf.Book': 1})
