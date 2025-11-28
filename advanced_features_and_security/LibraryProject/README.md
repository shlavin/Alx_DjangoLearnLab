# LibraryProject

##  Introduction

This project marks the beginning of learning Django web development. It involves setting up the Django environment, creating a new Django project named **LibraryProject**, and exploring its default structure.

The goal of this exercise is to understand the fundamental components that make up a Django project, how to run the development server, and how Django applications are organized.

---

##  Objective

Gain familiarity with Django by:

* Setting up a Django development environment.
* Creating and running a basic Django project.
* Understanding the structure and purpose of key Django files.

---

##  Setup Instructions

### 1. Install Python

Ensure that **Python** is installed on your system.
You can verify by running:

```bash
python --version
```

If Python is not installed, download and install it from [python.org/downloads](https://www.python.org/downloads/).

---

### 2. Install Django

Use `pip` (Python’s package manager) to install Django:

```bash
pip install django
```

To confirm installation:

```bash
django-admin --version
```

---

### 3. Create a New Django Project

Run the following command to create a project named **LibraryProject**:

```bash
django-admin startproject LibraryProject
```

This creates a directory named **LibraryProject** containing the default Django project structure.

---

### 4. Navigate to the Project Directory

```bash
cd LibraryProject
```

---

### 5. Run the Development Server

Start the Django development server by running:

```bash
python manage.py runserver
```

If successful, you’ll see a message similar to:

```
Starting development server at http://127.0.0.1:8000/
```

Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the default Django welcome page.

---

##  Project Structure Overview

After creating the project, the structure looks like this:

```
LibraryProject/
│
├── LibraryProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

### Key Files Explained

* **manage.py** — Command-line utility for interacting with the project (e.g., running the server, creating apps).
* **settings.py** — Contains all configurations for the Django project (database, installed apps, middleware, etc.).
* **urls.py** — Defines URL routing for the project.
* **wsgi.py / asgi.py** — Entry points for web servers to serve your project.
* **__init__.py** — Indicates that the directory should be treated as a Python package.

---

##  Repository Structure

**GitHub Repository:** `Alx_DjangoLearnLab`
**Directory:** `Introduction_to_Django`

---

##  Expected Output

After completing all steps, visiting [http://127.0.0.1:8000/](http://127.0.0.1:8000/) should display Django’s default welcome page, confirming that your setup is correct.

---

##  Next Steps

* Learn to create a Django app within the project.
* Understand Django models, views, and templates.
* Explore database configurations in `settings.py`.

---

**Author:** Shayani Nyambura Kahumu
**Course:** ALX Django Learn Lab
**Date:** 2nd November 2025
