#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip # https://docs.python.org/ja/3/library/gzip.html ファイルの圧縮、展開インターフェース
import json #jsonを扱うためのライブラリ

filename  = "jawiki-country.json.gz"
#reading modeでファイルを開く
with gzip.open(filename,'rt') as open_file:
    #1行ずつjsonファイルを読んで行く
    for text in open_file:
        #json文字列を辞書に変換
        jsondata = json.loads(text)
        #titleがイギリスだったら
        if jsondata['title'] == "イギリス":
            #本文を表示
            print(jsondata['text'])

