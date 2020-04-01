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

curl:
	curl -X GET -v 127.0.0.1:8080

curl/post: # docker で8080->3000につなぐ
	curl \
	-XPOST \
	-H 'Content-Type:application/json' \
	-d '{"message":"import numpy as np\nimport sys, os"}' \
	-v \
	127.0.0.1:8080

curl/server:
	curl -request POST \
	--header "Content-type:application/json" \
	-d '{"message":"import numpy as np\nimport sys,os"}' \
	-v \
	https://pisorts.denden.app/
