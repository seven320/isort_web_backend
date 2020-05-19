# READMD
[![CircleCI](https://circleci.com/gh/seven320/isort_web_backend.svg?style=svg&circle-token=99dfe5b61681e536d26e1d434f2ece9370854db0)](https://circleci.com/gh/seven320/isort_web_backend)



# isort_web
isortを使いやすいwebサービスにする

## Requirement
isort == 4.3.20
falcon == 2.0.0
pytest == 5.4.1
pytest-mock == 3.1.0

# 使い方
~~~
python3 main/src/server.py
~~~
サーバー起動
0.0.0.0:8080のポートに対してサーバーが起動する．

~~~
cd tests
make curl/local
~~~
でローカルでたったサーバーにリクエストを投げることができる．
# docker 
~~~
cd main
make re-run
~~~
これらによってisortを実行するdocker環境が立ち上がる
getting_library.pyでPipyから上位4000件のライブラリ名を見つけ出し，.isort.cfgファイルを更新する
このファイルをdockerにコピーすることでisortの設定を変更している．


