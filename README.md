# Sueweetbnb - Airbnb Clone Backend

A Django-based backend for an Airbnb clone project, built with Python 3.12 and Django 5.0.4.

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Poetry (Python package manager)

### Installation

1. Initialize Poetry and install dependencies

```bash
poetry config virtualenvs.in-project true --local
poetry install
poetry shell (only the first time)
```

2. Create Django project

```bash
django-admin startproject config .
```

3. Initialize database

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

## 🙏 Acknowledgments

- Based on [Nomadcoders Airbnb Clone](https://nomadcoders.co/airbnb-clone/lectures/3926)
- Inspired by [Airbnb](https://www.airbnb.com)
