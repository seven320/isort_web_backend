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


# COPY ./main /main

# isortのデフォルト設定を外部からコピー
# COPY setting/isort_setting.txt $XDG_CONFIG_HOME/.isort.cfg 
COPY src/* src/


EXPOSE 3000

RUN chmod +x ./src/
CMD ["python3", "./src/app.py"]
