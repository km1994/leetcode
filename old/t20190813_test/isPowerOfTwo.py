#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/13 
@url：https://leetcode-cn.com/problems/power-of-two/
@desc:
231. 2的幂
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

    示例 1:
        输入: 1
        输出: true
        解释: 20 = 1
    示例 2:
        输入: 16
        输出: true
        解释: 24 = 16
    示例 3:
        输入: 218
        输出: false



'''

class Solution:
    def __init__(self):
        pass
    
    def isPowerOfTwo1(self, n):
        if n == 0:
            return True
        while n%2 == 0:
            n = n/2
        if n == 1:
            return True
        return False

    # 不断除 2
    def isPowerOfTwo1(self, n):
        if n == 0:
            return True
        while n%2 == 0:
            n = n/2
        if n == 1:
            return True
        return False

if __name__ == "__main__":

text_list = []
text = input()
while(text!=''):
    text_list.append(text)
    text = input()

N,M =text_list[0].split(' ')
N = int(N)
M = int(M)
print(M)
print(N)
arr1 = [int(x) for x in text_list[1].split(' ')]
arr1_use = [False for _ in range(M)]
arr2 = [int(x) for x in text_list[2].split(' ')]
arr2_use = [False for _ in range(M)]
print(arr1)
print(arr2)
print(arr1_use)
print(arr2_use)
best_arr = []
for _ in range(M):
    for i in range(N):
        if not arr1_use[i]:
            best1 = i
    for j in range(N):
        if not arr2_use[j]:
            best2 = j
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if not arr1_use[i] and not arr2_use[j] and (arr1[i] + arr2[j])%N > (arr1[best1] + arr2[best2])%N:
                if len(best_arr)>0:
                    if best_arr[-1] < 4 and arr1[i] + arr2[j] >= N:
                        best1 = i
                        best2 = j
                    elif best_arr[-1] == 4 and arr1[i] + arr2[j] < N:
                        best1 = i
                        best2 = j
                elif (arr1[best1] + arr2[best2])%N:
                    best1 = i
                    best2 = j

    if not arr1_use[best1] and not arr2_use[best2]:
        arr1_use[best1] = True
        arr2_use[best2] = True
        if arr1[i] + arr2[j] >= N:
            best_arr[-1]+=1
        best_arr.append((arr1[best1] + arr2[best2])%N)

print(arr1_use)
print(arr2_use)
print(best_arr)

    


    
            


