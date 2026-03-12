install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

run:
	python manage.py runserver 8002

setup:
	pip install -r requirements.txt
	python manage.py migrate
