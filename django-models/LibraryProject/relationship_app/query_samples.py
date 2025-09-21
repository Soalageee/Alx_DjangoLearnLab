from relationship_app.models import Author, Book, Library, Librarian

# ----------------------
# Create sample data
# ----------------------
# Authors
Author.objects.create(name="George Orwell")
author_name = "George Orwell"
author = Author.objects.get(name=author_name)

# Books
Book.objects.create(title="1984", author=author)
Book.objects.create(title="Animal Farm", author=author)

# Library
Library.objects.create(name="Central Library")
library_name = "Central Library"
library = Library.objects.get(name=library_name)

# Add books to the library
library.books.add(*Book.objects.filter(author=author))

# Librarian
Librarian.objects.create(name="John Doe", library=library)

# ----------------------
# 1. Query all books by a specific author
# ----------------------
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:", list(books_by_author))

# ----------------------
# 2. List all books in a library
# ----------------------
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:", list(books_in_library))

# ----------------------
# 3. Retrieve the librarian for a library
# ----------------------
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}:", librarian)
