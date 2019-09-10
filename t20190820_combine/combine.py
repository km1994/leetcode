#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/20
@url：https://leetcode-cn.com/problems/combinations/
@desc:
    77. 组合
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

    示例:
    输入: n = 4, k = 2
    输出:
    [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]



'''

class Solution:
    def __init__(self):
        self.res_list = []
    
    def combine(self, n, k):
        if n < k:
            return False
        res = []
        self._dfs(n,k,1,[],res)
        return res

    def _dfs(self,n,k,start,pre,res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return
        for i in range(start,n+1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self._dfs(n,k,i+1,pre,res)
            # 回溯的时候，状态重置
            pre.pop()



        
   

if __name__ == "__main__":

    print("--------1-------")
    n = 4
    k = 2
    solution = Solution()
    res=solution.combine(n,k)
    print("res:{0}".format(res))

    print("--------2-------")
    n = 4
    k = 5
    solution = Solution()
    res=solution.combine(n,k)
    print("res:{0}".format(res))

    