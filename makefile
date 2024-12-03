build-dev:
	docker compose up --build -d --remove-orphans

build-prod:
	docker compose  -f docker-compose-deploy.yml up --build -d --remove-orphans

up:
	docker compose  up -d

down:
	docker compose down

migrate:
	docker compose run --rm app flask init-db

create-user:
	docker compose run --rm app flask create-user

seed-users:
	docker compose run --rm app flask seed-users --admin_count 2 --editor_count 5 --viewer_count 10 --password my_secure_password

seed-articles:
	docker compose run --rm app flask seed-articles --count 20

flake8:
	docker compose  exec app flake8 .

black-check:
	docker compose  exec app black --check .

black-diff:
	docker compose exec app black --diff .

black:
	docker compose exec app black .

isort-check:
	docker compose exec app isort . --check-only

isort-diff:
	docker compose exec app isort . --diff .

isort:
	docker compose exec app isort .