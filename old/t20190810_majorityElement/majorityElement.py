#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/10 
@url：https://leetcode-cn.com/classic/problems/majority-element/description/
@desc:
169. 求众数
    给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在众数。

    示例 1:
        输入: [3,2,3]
        输出: 3
    示例 2:
        输入: [2,2,1,1,1,2,2]
        输出: 2

'''
import math
class Solution:
    def __init__(self):
        pass
    
    # 摩尔投票法
    def majorityElement(self, nums):
        if not len(nums):
            return None
        candidate = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1
        return candidate


    # 利用 hash 进行存储 
    def majorityElement1(self, nums):
        element_dict = {}
        majority_level = math.floor(len(nums)/2)

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if num not in element_dict:
                element_dict[num] = 1
            else:
                element_dict[num] += 1
                if element_dict[num] > majority_level:
                    return num

    
if __name__ == "__main__":

    print("--------1-------")
    nums=[3,2,3]
    solution = Solution()
    res=solution.majorityElement(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums=[2,2,1,1,1,2,2]
    solution = Solution()
    res=solution.majorityElement(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums=[]
    solution = Solution()
    res=solution.majorityElement(nums)
    print("res:{0}".format(res))

    print("--------4-------")
    nums=[1]
    solution = Solution()
    res=solution.majorityElement(nums)
    print("res:{0}".format(res))
