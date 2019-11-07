#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/30
@url：https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
@desc:
    
    二维数组中的查找
    题目描述
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

    /* 思路
    * 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
    * 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
    * 要查找数字比左下角数字小时，上移

'''
import math
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row_len = len(array)
        col_len = len(array[0])
        i = row_len - 1
        j = 0
        while i > -1 and j < col_len:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                j = j + 1
            elif target < array[i][j]:
                i = i - 1
        return False
        
if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 = [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
        [4,5,6,7]
    ] 
    target = 8
    res=solution.Find(target,nums1)
    print("res:{0}".format(res))

    