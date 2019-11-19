#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/9 
@desc:
    用m种颜色着色圆的n个扇形的方法总数
    题目： 将圆分成 n 个扇形,用 m 种不同颜色染色,并且相邻的扇形不同色,问有多少种着色方法。


'''
import math

class Solution:
    def colorCount(self, n, m):
        if n <= 0 :
            return 0
        if n==1:
            return m
        ans = [0]
        ans.append(m)
        ans.append(m*(m-1))
        for i in range(3,n+1):
            ans.append(int(m*math.pow(m-1,n-1))-ans[i-1])
        return ans[-1]
    

if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    n = 5
    m = 4
    res=solution.colorCount(n,m)
    print(res)



    