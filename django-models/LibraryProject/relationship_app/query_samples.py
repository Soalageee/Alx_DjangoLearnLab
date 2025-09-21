from relationship_app.models import Author, Book, Library, Librarian

# ----------------------
# 1. Query all books by a specific author
# ----------------------
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)
print("Books by George Orwell:", list(author.books.all()))


# ----------------------
# 2. List all books in a library
# ----------------------
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)
print(f"Books in {library.name}:", list(library.books.all()))


# ----------------------
# 3. Retrieve the librarian for a library
# ----------------------
librarian = Librarian.objects.create(name="John Doe", library=library)
print(f"Librarian for {library.name}:", library.librarian)
