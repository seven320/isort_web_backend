build:
	docker build -t python:3.8-alpine-isort .

run:
	docker run -it --rm --name isort \
	-p 8001:8888 \
	python:3.8-alpine-isort /bin/sh
	
exec:
	docker exec -i -t isort /bin/bash
