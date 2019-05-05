#!/usr/bin/env python
# -*- coding: utf-8 -*-

file = 'hightemp.txt'
n = int(input("n="))
if n > 0:
    with open(file) as open_file:
        #readlines()は全ての行を読み込み行ごとのリストを取得
        lines = open_file.readlines()
    #pythonスライス負数の指定後ろからn行分を取得　https://qiita.com/tanuk1647/items/276d2be36f5abb8ea52e
    for line in lines[-n:]:
        print(line.rstrip())
