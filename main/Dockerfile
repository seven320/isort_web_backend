FROM python:3.8-alpine

RUN apk update && apk add ca-certificates

RUN pip install --upgrade pip
RUN pip install isort

# COPY ./main /main

# isortのデフォルト設定を外部からコピー
COPY setting/isort_setting.txt $XDG_CONFIG_HOME/.isort.cfg 
COPY src/* src/

EXPOSE 8001

