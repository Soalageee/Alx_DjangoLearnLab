from relationship_app.models import Author, Book, Library, Librarian

# Create author and books
Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=Author.objects.get(name="George Orwell"))
book2 = Book.objects.create(title="Animal Farm", author=Author.objects.get(name="George Orwell"))

# Retrieve the author by name
author_name = "George Orwell"
author = Author.objects.get(name=author_name)

# Query all books by this author
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:", list(books_by_author))
