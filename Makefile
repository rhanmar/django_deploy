build:
	docker-compose build

up:
	docker-compose  up

down:
	docker-compose down

exec_backend:
	docker-compose exec backend /bin/bash

test:
	docker-compose exec backend pytest

shell:
	docker-compose exec backend python manage.py shell
