# Bookshelf App - Permissions and Groups Setup

## Overview

This Django application manages a collection of books. User access is controlled using custom permissions and groups to ensure secure and role-based access to various features.

---

## Custom Permissions

The `Book` model includes the following custom permissions:

* **can_view**: Allows viewing the list of books.
* **can_create**: Allows creating new book entries.
* **can_edit**: Allows editing existing books.
* **can_delete**: Allows deleting books.

These are defined in `models.py` as:

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]
```

---

## Groups and Assigned Permissions

| Group   | Permissions Assigned                       |
| ------- | ------------------------------------------ |
| Viewers | can_view                                   |
| Editors | can_view, can_create, can_edit             |
| Admins  | can_view, can_create, can_edit, can_delete |

Users are assigned to these groups in the Django admin interface.

---

## Permission Enforcement

Permissions are enforced in views using the `@permission_required` decorator. For example:

```python
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    # Edit book logic
```

* Users lacking the required permission receive a **403 Forbidden** response.
* Login is required for all book actions using `@login_required`.

---

## Testing Approach

1. Create test users and assign them to the appropriate group.
2. Log in as each user and verify access:

| User Type | Accessible Actions               |
| --------- | -------------------------------- |
| Viewer    | View book list only              |
| Editor    | View, create, edit books         |
| Admin     | View, create, edit, delete books |

3. Attempt to access restricted URLs to ensure permissions are enforced correctly.


