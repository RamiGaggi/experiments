install:
	@poetry install

runserver:
	@poetry run python manage.py runserver 0.0.0.0:8000

migrations:
	@poetry run python manage.py makemigrations

migrate: migrations
	@poetry run python manage.py migrate

setup: migrate
	@echo Create a super user
	@poetry run python manage.py createsuperuser

requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt
