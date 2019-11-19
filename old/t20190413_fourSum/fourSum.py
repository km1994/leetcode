#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: isValid.py
@time: 2019/4/13 10:56
@desc:
    18. 四数之和
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

    注意：

        答案中不可以包含重复的四元组。

    示例：

        给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

        满足要求的四元组集合为：
            [
              [-1,  0, 0, 1],
              [-2, -1, 1, 2],
              [-2,  0, 0, 2]
            ]
'''


class Solution:
    def fourSum(self, nums, target):
        nums =sorted(nums)
        res=[]
        i=0
        j=0
        for i in range(len(nums)):
            if i==0 or nums[i]>nums[i-1]:
                for j in range(i+1,len(nums)):
                    if j==i+1 or nums[j] > nums[j-1] or nums[j] >nums [i]:
                        l=j+1
                        r=len(nums)-1
                        while l<r:
                            s = nums[i]+nums[j]+nums[l]+nums[r]
                            if s==target:
                                if [nums[i], nums[j], nums[l], nums[r]] not in res:
                                    res.append([nums[i], nums[j], nums[l], nums[r]])
                                l=l+1
                                r=r-1
                                while l<r and nums[l] == nums[l-1]:
                                    l=l+1
                                while l<r and nums[r]==nums[r+1]:
                                    r=r-1
                            elif s<target:
                                l=l+1
                            else:
                                r=r-1

        return res


if __name__ == "__main__":
    solution=Solution()
    res = solution.fourSum([-3,-2,-1,0,0,1,2,3],0)
    print("res:{0}".format(res))


