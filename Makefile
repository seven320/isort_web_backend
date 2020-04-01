compose/build:
	docker-compose build

compose/up:
	docker-compose up

re-run:
	docker-compose down
	docker-compose build --no-cache
	docker-compose up -d

compose/down:
	docker-compose down

logs:
	docker-compose logs
