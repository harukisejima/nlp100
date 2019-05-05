#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
def Typolycemia(text):
    result = []
    for word in text.split(' '):
        #文字の長さが4文字以下の場合
        if len(word) <= 4:
            #resultにそのまま追加
            result.append(word)
        else:
            #wordの1~-1を指定して抜き出す
            #pythonスライス負数の指定参照　https://qiita.com/tanuk1647/items/276d2be36f5abb8ea52e
            chr_list = list(word[1:-1])
            #shuffle関数で配列の中身をランダムにシャッフルする
            random.shuffle(chr_list)

            result.append(word[0] + ''.join(chr_list) + word[-1])
    
    return ' '.join(result)

#入力受付
text = input("文字列を入力してください。")

typo = Typolycemia(text)
print(typo)