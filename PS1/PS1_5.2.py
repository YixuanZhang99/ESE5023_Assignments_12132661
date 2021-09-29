# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:59:04 2021

@author: YixuanZhang1005
"""
import matplotlib.pyplot as plt

import numpy as np
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
            # print(expre)
            answer.append(expre)
    return len(answer)

Total_solutions = []
for i in range(0,101):
    Total_solutions.append(Find_expression(i))
print(Total_solutions)

max_index = np.argwhere(Total_solutions == np.amax(Total_solutions))
min_index = np.argwhere(Total_solutions == np.amin(Total_solutions))
max_index = max_index.flatten().tolist()
min_index = min_index.flatten().tolist()
print(max_index)
plt.plot(Total_solutions)
for i in range(len(max_index)):
    plt.plot(max_index[i],Total_solutions[max_index[i]],'ks')
    show_max='['+str(max_index[i])+', '+str(Total_solutions[max_index[i]])+']'
    plt.annotate(show_max,xytext=(max_index[i],Total_solutions[max_index[i]]),xy=(max_index[i],Total_solutions[max_index[i]]))
for i in range(len(min_index)):
    plt.plot(min_index[i],Total_solutions[min_index[i]],'gs')
    show_min='['+str(min_index[i])+', '+str(Total_solutions[min_index[i]])+']'
    plt.annotate(show_min,xytext=(min_index[i],Total_solutions[min_index[i]]),xy=(min_index[i],Total_solutions[min_index[i]]))
plt.show()
