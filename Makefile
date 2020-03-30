compose/build:
	docker-compose build

compose/up:
	docker-compose up

compose:
	docker-compose down
	docker-compose build --no-cache
	docker-compose up -d

compose/down:
	docker-compose down
