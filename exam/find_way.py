#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dfs(l, x, y):
    global result
    print(len(l))
    print(len(l[x]))
    if x+1 < len(l) and y+1 < len(l[x]):
        print(l[x+1][y])
        if l[x+1][y] != 1:


        if l[x][y+1] != 1:


        dfs(l, x+1, y)
        dfs(l, x, y+1)

a = input()
result = 0
x = 0
y = 0
dfs(a, x, y)
print(result)
