#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

file = 'hightemp.txt'
n = int(input("n="))

with open(file) as open_file:
    lines = open_file.readlines()
count = len(lines)#全体は24行
#ceilは https://docs.python.org/ja/3/library/math.html (count/n)以上の最小の整数
unit = math.ceil(count/n)#1ファイルあたりの行数
#0から最後までunitずつ回す iは1から始める
for i, ofset in enumerate(range(0,count,unit),1):
    #1~?番目までファイルをファイルを作るためにformatを使用
    with open('child_{}.txt'.format(i), mode='w') as out_file:
        #lineにlinesを分割した分を入れていく
        for line in lines[ofset:ofset + unit]:
            #ファイルの書き込み
            out_file.write(line)
