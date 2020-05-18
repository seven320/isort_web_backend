curl/local:
	curl -X GET -vv 0.0.0.0:8080

curl/local/wrong:
	curl -X GET -vvv 0.0.0.0:8080/image

curl/local/post:
	curl -POST \
	-H 'Content-Type:application/json' \
	-d '{"message":"import a\nimport z\nimport az"}' \
	-vv \
	0.0.0.0:8080

curl:
	curl -X GET -v 127.0.0.1:3000

curl/post:
	curl \
	-XPOST \
	-H 'Content-Type:application/json' \
	-d '{"message":"impor"}' \
	-v \
	127.0.0.1:3000
	
test:
	python3 test_app.py

