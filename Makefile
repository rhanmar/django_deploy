build:
	docker-compose build

up:
	docker-compose  up

down:
	docker-compose down

exec_backend:
	docker-compose exec backend /bin/bash

exec_db:
	docker-compose exec db /bin/bash

test:
	docker-compose exec backend pytest

shell:
	docker-compose exec backend python manage.py shell

migrate:
	docker-compose exec backend python manage.py migrate

fill_db:
	docker-compose exec backend python manage.py fill_db
