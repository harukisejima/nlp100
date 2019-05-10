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
    


        
