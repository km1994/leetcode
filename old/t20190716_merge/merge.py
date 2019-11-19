#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: merge.py
@time: 2019/7/16
@rel： https://leetcode-cn.com/problems/merge-intervals/
@url：
@desc:
    56. 合并区间
    给出一个区间的集合，请合并所有重叠的区间。

    示例 1:
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

    示例 2:
    输入: [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''
class Solution:
    def __init__(self):
        pass

    def merge(self, intervals):
        intervals = sorted(intervals)
        res_list = []

        if len(intervals) == 0:
            return intervals

        res_list.append(intervals[0])

        for i in range(1,len(intervals)):
            if res_list[-1][-1] >= intervals[i][0]:
                res_list[-1][-1] = max(res_list[-1][-1],intervals[i][-1])
            else:
                res_list.append(intervals[i])

        return res_list


if __name__ == "__main__":

    solution = Solution()

    arr1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res1 = solution.merge(arr1)
    print("res1:{0}".format(res1))

    arr2 = []
    res2 = solution.merge(arr2)
    print("res2:{0}".format(res2))

    arr3 = [[1,4],[4,5]]
    res3 = solution.merge(arr3)
    print("res3:{0}".format(res3))

    arr4 = [[1, 4]]
    res4 = solution.merge(arr4)
    print("res4:{0}".format(res4))

    arr5 = [[1,4],[0,4]]
    res5 = solution.merge(arr5)
    print("res5:{0}".format(res5))

    arr6 = [[3, 5], [8, 10], [1, 3], [15, 18]]
    res6 = solution.merge(arr6)
    print("res6:{0}".format(res6))

    arr7 = [[1,4],[0,2],[3,5]]
    res7 = solution.merge(arr7)
    print("res7:{0}".format(res7))









    

