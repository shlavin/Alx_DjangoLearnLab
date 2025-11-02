# Retrieve Operation

**Objective:** Retrieve and display all attributes of the book created in the previous step.

**Python Command:**

```python
from bookshelf.models import Book
books = Book.objects.all()
for b in books:
    print(b.id, b.title, b.author, b.publication_year)
```

**Expected Output:**

```python
# Output:
1 1984 George Orwell 1949
# The details of the created book are successfully displayed.
```
