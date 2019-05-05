#!/usr/bin/env python
# -*- coding: utf-8 -*-
file = 'hightemp.txt'
count = 0
#with構文について https://www.sejuku.net/blog/24672
#open関数を使用してファイルが存在しない場合は新規に作成される mode=書き込み
with open('col1.txt') as col1_file,open('col2.txt') as col2_file,open('merge.txt',mode='w') as merge:
    for col1,col2 in zip(col1_file,col2_file):
        #rstrip()引数を与えなかったら文字列の最後の空白を消去してくれる
        merge.write(col1.rstrip() + '\t' + col2.rstrip() + '\n')