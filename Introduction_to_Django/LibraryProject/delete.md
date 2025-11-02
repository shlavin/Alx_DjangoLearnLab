# Delete Operation

**Objective:** Delete the created book and confirm the deletion by retrieving all books again.

**Python Command:**

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

**Expected Output:**

```python
# Output:
(1, {'bookshelf.Book': 1})
<QuerySet []>
# The book has been successfully deleted and the database is now empty.
```
