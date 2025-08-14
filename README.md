# Django REST API for Clients & Projects

A simple Django REST Framework API to manage **Clients**, **Projects**, and **Users**.

## Features
- Register and fetch clients.
- Create, update, and delete projects.
- Assign multiple users to a project.
- Auto-track project creator and creation date.

## Technologies
- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite 

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/your-repo.git
cd project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
