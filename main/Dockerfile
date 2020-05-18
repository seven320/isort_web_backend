FROM python:3.8-alpine

MAINTAINER KenKato <github: seven320>

RUN apk update && apk --no-cache add \
    ca-certificates \
    make \
    curl

RUN pip install --upgrade pip
RUN pip install \
    isort==4.3.20 \
    falcon==2.0.0

# isortのデフォルト設定を外部からコピー
COPY src/* src/
COPY setting/.isort.cfg ~/.isort.cfg

EXPOSE 8080

RUN chmod +x ./src/
CMD ["python3", "./src/server.py"]
