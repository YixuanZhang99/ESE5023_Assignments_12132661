# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:00:49 2021

@author: YixuanZhang1005
"""
def Least_moves(x):
    step = 0
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x -= 1
        step += 1
    print(step)
            