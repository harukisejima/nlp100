#!/usr/bin/env python
# -*- coding: utf-8 -*-
#n-gramとは隣り合うn個の塊のことを表すらしい
str = "I am an NLPer"
#n_gramを返す関数
def n_gram(word,n=2):
    result = []
    #隣あった文字同士なので全体量-n+1分回す。
    for i in range(0,len(word)-n+1):
        #reultにi番目からn個ずつ抜き取り格納する
        result.append(word[i:i+n])
    return result
#文字列str
str = "I am an NLPer"
#strを空白で分けてwordsに格納する
words = str.split(" ")
# 単語
result = n_gram(words, 1)
print(result)
#文字
char = n_gram(str,1)
print(char)
'''
スライスの復習
https://qiita.com/tanuk1647/items/276d2be36f5abb8ea52e
'''