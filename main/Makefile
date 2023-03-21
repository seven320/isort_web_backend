stop:
	docker stop isort 

build:
	docker build -t python:3.8-alpine-isort --no-cache .

run:
	docker run -it --rm --name isort \
	-p 8080:8080 -d \
	python:3.8-alpine-isort
	
re-run:
	make build run

exec:
	docker exec -i -t isort /bin/sh

get:
	curl -H "Authorization: Bearer <<>>" -v http://localhost:8080

post:
	curl -request POST \
	-d '{"message":"import numpy as np\nimport sys,os"}' \
	-v http://localhost:8080/ \
	--header "Content-type:application/json" \
	--header "Authorization: kBearer <<>>" \