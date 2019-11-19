#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/26
@url：
@desc:
    请设计一个算法，在满足质因数仅为3,5,7或其组合的数中，找出第K大的数。
    比如K=1,2,3时，分别应返回3,5,7。要求算法时间复杂度最优。

    解法：
        这道题其实是一个分段函数：
            K = 1 : f(K) = 3
            K = 2 : f(K) = 5
            K = 3 : f(K) = 7
            K > 3 : f(K) = f(K-2) + f(K-3)

'''
import math
class Solution:
    # 递归法
    def Kmax(self, K):
        if K == 1:
            return 3
        elif K == 2:
            return 5
        elif K == 3:
            return 7
        else:
            return self.Kmax(K-2) + self.Kmax(K-3)
        
if __name__ == "__main__":

    print("--------1-------")
    K = 6
    solution = Solution()
    res=solution.Kmax(K)
    print("res:{0}".format(res))

    # print("--------2-------")
    # nums = []
    # solution = Solution()
    # res=solution.subsets(nums)
    # print("res:{0}".format(res))

    