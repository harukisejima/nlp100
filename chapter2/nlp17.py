#!/usr/bin/env python
# -*- coding: utf-8 -*-

file = 'hightemp.txt'
with open(file) as open_file:
    #集合
    sets = set()
    for line in open_file:
        #tabで区切ってcolに格納
        col = line.split('\t')
        #colの0番目をsetsに追加
        sets.add(col[0])
#setsの中身を表示
for i in sets:
    print(i)