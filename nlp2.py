#!/usr/bin/env python
# -*- coding: utf-8 -*-
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = []
#空白文字で分けてwordリストに一個づず格納
word = str.split(" ")
#wordの要素数分回す
for i in word:
    #resultに「,」と「.」を除いた数を追加していく
    result.append(len(i)-i.count(",")-i.count("."))
    #結果の表示
print(result)