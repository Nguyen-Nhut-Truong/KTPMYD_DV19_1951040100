# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:10:37 2021

@author: DELL
"""

def KT(arr):
    count =0
    for i in arr:
        if(i<2):
            count=count+1
        else:
            for j in range (2,i-1):
                if(i%j==0 and j<i):
                    count= count+1
                    break
    return len(arr)-count
a= [6,7,13,17]
print(KT(a))
