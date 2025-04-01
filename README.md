poetry init
poetry add django -> create poetry.lock
poetry shell

django-admin
django-admin startproject config .

gitignore extension -> open palette -> gitignore -> python -> create
setup.md -> into .gitignore

python manage.py runserver
ctrl+c
python manage.py migrate
python manage.py createsuperuser

python manage.py startapp houses

- migration for houses
  python manage.py makemigrations
  python manage.py migrate

poetry add pillow

# Django documentation link: https://docs.djangoproject.com/en/5.0/

Must replace user model with custom user model

python managy.py startapp users -> Must do this from the beginning, when there is no user.

- in the mid-project, delete database, "001_initial.py, 002_initial.py"
- Don't delete migrations folder and **init**.py

# migration: sync database structure with model structure in python code (models.py)

# Django ORM 
https://docs.djangoproject.com/en/5.1/ref/models/instances/
https://docs.djangoproject.com/en/5.1/topics/db/queries/ 
python manage.py shell
connect to the database

# VScode extension

- SQLite viewr
- Black fomatter

If you want to set up an interpreter in poetry, you can type command "poetry env use python"
then put that location in the interpreter pallette.

[tool.poetry]
name = "airbnb-clone"
version = "0.1.0"
description = ""
authors = ["feelsuegood <suaj2021@gmail.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django = "^5.0.4"
pillow = "^10.3.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
