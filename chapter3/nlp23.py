#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json
import re

def chose_text():
    filename = "jawiki-country.json.gz"
    #reading modeでファイルを開く
    with gzip.open(filename,'rt') as open_file:
        #一行ずつjsonファイルをよんでいく
        for text in open_file:
            #json文字列を辞書に変更
            jsondata = json.loads(text)
            #titleがイギリスだったら
            if jsondata['title'] == 'イギリス':
                #本文を表示
                return jsondata['text']

#正規表現のコンパイル
#{n,}n回以上の繰り返しにマッチする表現ここでは=が2回以上の繰り返しとする
#\sが空白文字を表している。*が0回以上の繰り返しなので空白文字、0回以上の繰り返しこれはキャプチャ対象外
#.が任意の1文字で+が一回以上の繰り返し、?はちょっとよくわかんないんだけど手前の==交通の邪魔を避けるためっぽい後で考えよう
#\s*余分な0個以上の空白を除去する
#\1後方参照、完全には理解していないけどおそらく(={2,})を参照している

pattern  = re.compile(r'^(={2,})\s*(.+?)\s*\1$', re.MULTILINE + re.VERBOSE)

#抽出
result = pattern.findall(chose_text())
print(result)
for line in result:
    #=の数-1がレベルになるから
    level = len(line[0])-1
    print("{section}{level}".format(section=line[1],level=level))