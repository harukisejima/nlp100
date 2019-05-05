#!/usr/bin/env python
# -*- coding: utf-8 -*-
file = 'hightemp.txt'
count = 0
#with構文について https://www.sejuku.net/blog/24672
with open(file) as data_file:
    for line in data_file:
        count+=1
print(count)