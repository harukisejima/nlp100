# -*- coding: utf-8 -*-
str1 = "パトカー"
str2 = "タクシー"
result = ""
#str1,str2を1文字ずつi,jに格納しながらforをstr1,2分回す
for i,j in zip(str1,str2):
    #resultにi,jをくっつけたのを追加
    result += i+j
#出力
print(result)