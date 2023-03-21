compose/build:
	docker-compose build

compose/up:
	docker-compose up

re-run:
	python3 main/setting/get_libraries.py
	docker-compose down
	docker-compose build --no-cache
	docker-compose up -d

compose/down:
	docker-compose down

logs:
	docker-compose logs

test:
	docker-compose down
	docker-compose build 
	docker-compose up -d
	docker exec isort pytest tests
	docker-compose down