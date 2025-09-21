```markdown
# Update Operation

```python
from bookshelf.models import Book

# Update book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Retrieve all books
Book.objects.all()
# Expected Output:
# <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
