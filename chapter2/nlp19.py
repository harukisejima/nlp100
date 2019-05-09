#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
file = 'hightemp.txt'
with open(file) as open_file:
    # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    lines = open_file.readlines()
    # 県だけを取り出してkensに格納する
    kens = [line.split('\t')[0]for line in lines]
    # Counterを使って頻出頻度を調べる
    count = collections.Counter(kens)
    # count.most_commo()がタプルで（要素:頻出頻度）で返して来るので一つずつ取り出す
    for w,c in count.most_common():
        # 表示
        print(w,c)

