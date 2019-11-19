#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/5/20
@rel： https://leetcode-cn.com/problems/longest-valid-parentheses/
@url：
@desc:
    32. 将一个数组四等分，让四份和尽可能相差很小
    将一个数组四等分，让四份和尽可能相差很小


'''


class Solution:
    def __init__(self, arr):
        self.arr = arr

    def  zuiyouhua(self, arr) :
        self.QuickSort(0,len(arr)-1)
        return [self.arr[i] for i in range(0,len(self.arr),4)],[self.arr[i] for i in range(1,len(self.arr),4)],[self.arr[i] for i in range(2,len(self.arr),4)],[self.arr[i] for i in range(3,len(self.arr),4)]

    def QuickSort(self,left,right):
        if left < right:
            pivot = self.Partition(left,right)
            self.QuickSort(left,pivot-1)
            self.QuickSort( pivot+1,right)

    def Partition(self,left,right):
        pivot = self.arr[left]
        while left < right:
            while left < right and pivot < self.arr[right]:
                right = right - 1
            self.arr[left] = self.arr[right]
            while left < right and pivot >= self.arr[left]:
                left = left +1
            self.arr[right] = self.arr[left]
        self.arr[left] = pivot
        return left



if __name__ == "__main__":
    arr=[7,4,2,5,2,5,8,3]
    print("arr:{0}".format(arr))
    solution = Solution(arr)
    a1,a2,a3,a4 = solution.zuiyouhua(arr)
    print("solution.arr:{0}".format(solution.arr))
    print("a1:{0},a2:{1},a3:{2},a4:{3}".format(a1,a2,a3,a4))
    # solution.QuickSort(0,len(arr)-1)
    # print("solution.arr:{0}".format(solution.arr))

