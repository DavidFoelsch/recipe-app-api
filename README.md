# recipe-app-api
Recipe API project

## Reminders:
To setup project use:
docker-compose run --rm app sh -c "django-admin startproject app ."

For linter only use:
docker-compose run --rm app sh -c "flake8"

For build
docker-compose build

For run test
docker compose run --rm app sh -c "python manage.py test"