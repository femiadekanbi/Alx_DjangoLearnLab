from bookshelf.models import Book

# Retrieve the book we want to delete
book_to_delete = Book.objects.get(title="1984")

# Delete the book
book_to_delete.delete()

# Confirm deletion
print(Book.objects.all())  # The deleted book will no longer appear
