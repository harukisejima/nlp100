#!/usr/bin/env python
# -*- coding: utf-8 -*-

file = 'hightemp.txt'
with open(file) as open_file:
    lines = open_file.readlines()
    #sort関数でreverseをtrue 2番目の要素をkeyとして扱うためlambda
    lines.sort(key=lambda line: float(line.split('\t'[2]),reversed=True))
#sort後の表示
for line in lines:
    print(line, end='')