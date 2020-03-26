# isort_web
isortを使いやすいwebサービスにする


# docker 
~~~
cd main

make re-run

~~~
これらによってisortを実行するdocker環境が立ち上がる
getting_library.pyでPipyから上位4000件のライブラリ名を見つけ出し，.isort.cfgファイルを更新する
このファイルをdockerにコピーすることでisortの設定を変更している．

