FROM python:3.8-alpine

RUN apk update && apk --no-cache add \
    ca-certificates \
    make 

RUN pip install --upgrade pip
RUN pip install \
    isort==4.3.21 \
    falcon==2.0.0


# COPY ./main /main

# isortのデフォルト設定を外部からコピー
# COPY setting/isort_setting.txt $XDG_CONFIG_HOME/.isort.cfg 
COPY src/* src/

EXPOSE 8001
