#!/usr/bin/env python
# -*- coding: utf-8 -*-
file = 'hightemp.txt'
count = 0
#with構文について https://www.sejuku.net/blog/24672
#open関数を使用してファイルが存在しない場合は新規に作成される mode=書き込み
with open(file) as data_file,open('col1.txt', mode='w') as col1_file,open('col2.txt', mode='w') as col2_file:
    for line in data_file:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')