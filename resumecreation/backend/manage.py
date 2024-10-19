#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ResumeCreation.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


'''
> python manage.py makemigrations CVBuilder
> python manage.py migrate
> python manage.py runserver
> python manage.py createsuperuser
> http://127.0.0.1:8000/admin/
> http://127.0.0.1:8000/api/admin/users/
> http://127.0.0.1:8000/api/token/
'''
if __name__ == '__main__':
    main()
