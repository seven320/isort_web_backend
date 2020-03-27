build:
	python3 setting/get_libraries.py
	docker build -t python:3.8-alpine-isort --no-cache .

run:
	docker run -it --rm --name isort \
	-p 8080:3000 -d \
	python:3.8-alpine-isort
	
re-run:
	make build run

exec:
	docker exec -i -t isort /bin/sh
