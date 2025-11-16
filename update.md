from bookshelf.models import Book

# Retrieve the book we want to update
book_to_update = Book.objects.get(title="1984")

# Update the author
book_to_update.author = "G. Orwell"

# Save changes to the database
book_to_update.save()

# Confirm update
print(book_to_update)  # <Book: 1984 by G. Orwell (1949)>
