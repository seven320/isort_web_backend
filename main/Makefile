build:
	docker build -t python:3.8-alpine-isort --no-cache .

run:
	docker run -it --rm --name isort \
	-p 8080:8080 -d \
	python:3.8-alpine-isort
	
re-run:
	make build run

exec:
	docker exec -i -t isort_web_backend_pisort_1 /bin/sh


curl/server:
	curl -request POST \
	--header "Content-type:application/json" \
	-d '{"message":"import numpy as np\nimport sys,os"}' \
	-v \
	https://pisorts.denden.app/
