# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:31:43 2021

@author: YixuanZhang1005
"""

def Find_expression(x):
    num = '123456789'
    sign = ['+', '-', ' ']
    sign_line = ''
    last_sign = ['+', '-', ' ']
    all_sign = []
    answer = []
    for i in range(7):
        new_sign = []
        for j in range(3):
            for k in range(len(last_sign)):
                sign_line = last_sign[k] + sign[j]
                new_sign.append(sign_line)
        last_sign = new_sign
        all_sign = new_sign

    for i in range(len(new_sign)):
        expre = '1'
        for j in range(8):
            if new_sign[i][j] == ' ':
                expre = expre + num[j+1]
            else:
                expre = expre + new_sign[i][j] + num[j+1]
        if eval(expre) == x:
            expre = expre + '=' + str(x)
            print(expre)
            answer.append(expre)
