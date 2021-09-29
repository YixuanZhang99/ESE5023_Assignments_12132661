# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:29:13 2021

@author: YixuanZhang1005
"""
# k start from 0
def triangles(k):
    if k <= 0:
        print("please input number > 0")
    else:
        k = k-1
        L = []
        l = [1]
        L.append(l)
        index = 0
        while index < k:
            index += 1
            l.append(0)
            l = [l[i-1] + l[i] for i in range(0,len(l))]
            L.append(l)
        print(L[k])
