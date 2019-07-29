#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: generateMatrix.py
@time: 2019/7/24
@rel： https://leetcode-cn.com/problems/spiral-matrix-ii/
@url：
@desc:
    42. 接雨水


'''
class Solution:
    def __init__(self):
        pass

    def trap(self, height):
        if len(height) == 0:
            return 0
        ans = 0
        height_len = len(height)
        left_max = []

        left_max.append(height[0])
        for i in range(1,height_len):
            left_max.append(max(height[i],left_max[i-1]))

        right_max = []
        right_max.append(height[height_len-1])
        for i in range(height_len-2,-1,-1):
            right_max.append(max(height[i],right_max[height_len-i-2]))

        for i in range(1,height_len-1):
            ans = ans + min(left_max[i],right_max[height_len-i-1]) - height[i]
        return ans


if __name__ == "__main__":

    solution = Solution()

    n = [0,1,0,2,1,0,1,3,2,1,2,1]
    res1 = solution.trap(n)
    print("res1:{0}".format(res1))






    

