#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/9 
@url：https://leetcode-cn.com/problems/single-number/
@desc:
    136. 只出现一次的数字
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

    示例 1:
        输入: [2,2,1]
        输出: 1
    示例 2:
        输入: [4,1,2,1,2]
        输出: 4

'''

class Solution:
    def __init__(self):
        pass
    
    # 位运算
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans


    # 用一个桶来存储出现一次的数字，当再次出现时，就讲该数字删除
    def singleNumber2(self, nums):
        if not len(nums):
            return None
        one_list = []
        for num in nums:
            if num not in one_list:
                one_list.append(num)
            else:
                one_list.remove(num)
        return one_list[0]


    # 构建两个桶来分别存储出现一次和出现两次的数字
    def singleNumber1(self, nums):
        if not len(nums):
            return None
        one_dict = {}
        one_dict[1]=[]
        one_dict[2]=[]
        for num in nums:
            if num not in one_dict[1]:
                one_dict[1].append(num)
            else:
                one_dict[2].append(num)
                one_dict[1].remove(num)
        
        return one_dict[1][0]
        

if __name__ == "__main__":

    print("--------1-------")
    nums=[2,2,1]
    solution = Solution()
    res=solution.singleNumber(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums=[4,1,2,1,2]
    solution = Solution()
    res=solution.singleNumber(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums=[]
    solution = Solution()
    res=solution.singleNumber(nums)
    print("res:{0}".format(res))
