#!/usr/bin/env python
# -*- coding: utf-8 -*-

#n_gramを返す関数
def n_gram(word,n=2):
    result = []
    #隣あった文字同士なので全体量-n+1分回す。
    for i in range(0,len(word)-n+1):
        #reultにi番目からn個ずつ抜き取り格納する
        result.append(word[i:i+n])
    return result

#set型:pythonに標準で用意されている集合を扱う型
set_x = set(n_gram("paraparaparadise"))
set_y = set(n_gram("paragraph"))
print("集合x:",str(set_x))
print("集合y:",str(set_y))

#和集合
set_or = set_x | set_y
#積集合
set_and = set_x & set_y
#差集合
set_sub = set_x - set_y

print("和集合:",set_or)
print("積集合:",set_and)
print("差集合:",set_sub)

#seが含まれるかどうか
print("seがXに含まれる:",str("se" in set_x))
print("seがYに含まれる:",str("se" in set_y))