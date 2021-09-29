# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:24:32 2021

@author: YixuanZhang1005
"""
import numpy as np
M1 = np.mat(np.random.randint(51, size=(5,10)))
M2 = np.mat(np.random.randint(51, size=(10,5)))
print(M1, '\n', M2)
def Matrix_multip(M1, M2):
    new_matrix = np.mat(np.zeros([M1.shape[0], M1.shape[0]], int))
    for i in range(M1.shape[0]):
        for j in range(M2.shape[1]):
            tmp = 0
            for k in range(M1.shape[1]):
                tmp += M1[i,k] * M2[k,j]
                new_matrix[i,j] = tmp
    return new_matrix

print(Matrix_multip(M1, M2))