#!/usr/bin/env python
# -*- coding: utf-8 -*-
file = 'hightemp.txt'
count = 0
#with構文について https://www.sejuku.net/blog/24672
with open(file) as data_file:
    for line in data_file:
        #end=''は改行なし出力
        #replace関数 https://techacademy.jp/magazine/19188
        print(line.replace('\t',' '), end='')