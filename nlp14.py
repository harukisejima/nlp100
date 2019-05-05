#!/usr/bin/env python
# -*- coding: utf-8 -*-

file = 'hightemp.txt'

n = int(input("n="))
with open(file) as open_file:
    for i,line in enumerate(open_file):
        if n == i:
            break
        print(line)