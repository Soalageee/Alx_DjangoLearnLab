```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check all books
Book.objects.all()
# Expected Output:
# <QuerySet []>
