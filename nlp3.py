#!/usr/bin/env python
# -*- coding: utf-8 -*-
#一個目だけ抜き出すタプル
first_num = (1, 5, 6, 7, 8, 9, 15, 16, 19)
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
#結果を格納する辞書
result = {}
#空白文字で区切ってwordに格納
word = str.split(" ")
for num,i in enumerate(word,1):
    #enumurate https://note.nkmk.me/python-enumerate-start/
    if num in first_num:
        #単語の1文字目を抜いきとってresultに格納する
        result[i[0:1]] = num
    else:
        #単語の2文字目までを抜いきとってresultに格納する
        result[i[0:2]] = num
#結果を出力
print(result)