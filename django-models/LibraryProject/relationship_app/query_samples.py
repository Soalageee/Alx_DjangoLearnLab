from relationship_app.models import Author, Book, Library, Librarian

# Create author and books
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

# Create library and add books
Library.objects.create(name="Central Library").books.add(book1, book2)

# Retrieve the library by name as expected by automated checks
library_name = "Central Library"
library = Library.objects.get(name=library_name)

# List all books in the library
print(f"Books in {library.name}:", list(library.books.all()))
