# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:16:40 2021

@author: YixuanZhang1005
"""
def Print_values(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        elif a > c:
            print(a, c, b)
        else:
            print(c, a, b)
    elif b > c:
            print('null')
    else:
            print(c, b, a)
