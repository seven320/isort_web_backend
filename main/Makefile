build:
	python3 setting/get_libraries.py
	docker build -t python:3.8-alpine-isort .

run:
	docker run -it --rm --name isort \
	-p 8001:8888 \
	python:3.8-alpine-isort /bin/sh
	
re-run:
	make build run

exec:
	docker exec -i -t isort /bin/bash
