# Airbnb Clone Backend

A Django-based backend for an Airbnb clone project, built with Python 3.12 and Django 5.0.4.

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Poetry (Python package manager)

### Installation

1. Initialize Poetry and install dependencies

```bash
poetry config virtualenvs.in-project true
poetry install
poetry shell
```

If you want to set up an interpreter in poetry, you can type command:

```bash
poetry env use python
```

2. Create Django project

```bash
django-admin startproject config .
```

3. Set up development environment

- Create .gitignore file for Python projects
- Install VSCode extensions:
  - SQLite viewer
  - Black formatter

4. Initialize database

```bash
python manage.py migrate
python manage.py createsuperuser
```

## 📦 Project Structure

- `users/` - Custom user model and authentication
- `rooms/` - Room listings and management
- `experiences/` - Experience listings
- `bookings/` - Booking system
- `reviews/` - Review system
- `wishlists/` - User wishlists
- `direct_messages/` - Messaging system
- `medias/` - Media file handling
- `common/` - Shared utilities and configurations

## 🔧 Development

### Creating New Apps

```bash
python manage.py startapp [app_name]
```

### Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the Server

```bash
python manage.py runserver
```

## ⚠️ Important Notes

- Custom user model must be implemented at the beginning of the project
- If modifying user model mid-project:
  - Delete database
  - Remove initial migration files (001_initial.py, 002_initial.py)
  - Keep migrations folder and **init**.py

## 📚 Documentation

- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
- [Django ORM Documentation](https://docs.djangoproject.com/en/5.1/ref/models/instances/)
- [Django Queries Documentation](https://docs.djangoproject.com/en/5.1/topics/db/queries/)

## 🛠️ Tech Stack

- Python 3.12
- Django 5.0.4
- Pillow 10.3.0 (Image processing)
- Poetry (Dependency management)

## 🙏 Acknowledgments

- Based on [Nomadcoders Airbnb Clone](https://nomadcoders.co/airbnb-clone/lectures/3926)
- Inspired by [Airbnb](https://www.airbnb.com)
