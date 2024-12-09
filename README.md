# django_todo Project Setup and Run Guide

This README provides step-by-step instructions for setting up and running the django_todo project.
The project includes a todo app and uses db.sqlite3 as the database backend.

## Prerequisites

Ensure you have the following installed:

1). Python (Version 3.8 or higher)
2). pip (Python package manager)
3). virtualenv (optional but recommended)

## Steps to Set Up and Run the Project

### 1. Clone the Repository
Clone the project repository to your local machine:

```
git clone https://github.com/ShadowAdi/django_assignment.git
cd django_todo
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment for this project to avoid dependency conflicts:
```
python -m venv env
source env/bin/activate      # For Linux/Mac
env\Scripts\activate         # For Windows
```

### 3.  Install Dependencies

Install the required Python packages:

```
pip install django
```

### 4. Configure the Database

By default, the project uses db.sqlite3, which is already set up. You do not need to make additional configurations.


### 5. Run Migrations

Apply database migrations to set up the Todo model:
```
python manage.py makemigrations todo
python manage.py migrate
```

### 6. Run the Development Server
Start the Django development server:

```
python manage.py runserver
```
Access the application in your browser at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Using the Application

### Adding a New Task

Navigate to the  `todoCreate` page to create a new task. Fill out the form and submit.

### Viewing Tasks

All tasks will be displayed on the /todo/ page.

## Contact

For any issues or inquiries, feel free to contact the project maintainer:

* Name: Aditya Shukla
* Email: shadowshukla76@gmail.com
* GitHub: [ShadowAdi](https://github.com/ShadowAdi)


