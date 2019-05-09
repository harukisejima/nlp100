#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip # https://docs.python.org/ja/3/library/gzip.html ファイルの圧縮、展開インターフェース
import json #jsonを扱うためのライブラリ
import re #正規表現を扱うライブラリ

def chose_text():  
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
                return jsondata['text']

# 正規表現のコンパイル
#[[Category:と]]で括られている
pattern = re.compile(r'^ \[\[Category:.*\]\]$', re.MULTILINE + re.VERBOSE)
# 抽出
result = pattern.findall(chose_text())

# 結果表示
for line in result:
    print(line)