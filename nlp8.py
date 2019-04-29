#!/usr/bin/env python
# -*- coding: utf-8 -*-

def angou(text):
    result = ""
    for i in text:
        if i.islower():
            result += chr(219 - ord(i))
        else:
            result += i
    return result


#文字列の入力受付
text = input("文字列入力")

#暗号化
enc = angou(text)
print("暗号化後:"+enc)
dec = angou(enc)
print("復号化後:"+dec)



