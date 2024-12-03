build-dev:
	docker compose up --build -d --remove-orphans

build-prod:
	docker compose up -f docker-compose-deploy.yml --build -d --remove-orphans

up:
	docker compose  up -d

down:
	docker compose down

migrate:
	docker compose -f local.yml run --rm api flask init-db

create-user:
	docker compose -f local.yml run --rm api flask create-user

seed-users:
	docker compose -f local.yml run --rm api flask seed-users --admin_count 2 --editor_count 5 --viewer_count 10 --password my_secure_password

seed-articles:
	docker compose -f local.yml run --rm api flask seed-articles --count 20
