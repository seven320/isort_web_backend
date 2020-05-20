FROM python:3.8-alpine

MAINTAINER KenKato <github: seven320>

RUN apk update && apk --no-cache add \
    ca-certificates \
    make \
    curl

RUN pip install --upgrade pip
RUN pip install \
    isort==4.3.20 \
    falcon==2.0.0 \
    pytest==5.4.1 \
    pytest-mock==3.1.0 \
    requests==2.23.0

# isortのデフォルト設定を外部からコピー
COPY setting/* setting/
COPY tests/* tests/
COPY src/* src/
COPY setting/.isort.cfg $XDG_CONFIG_HOME/.isort.cfg

EXPOSE 8080

RUN chmod +x ./src/
CMD ["python3", "src/server.py"]