#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/22
@url：https://leetcode-cn.com/problems/jump-game/
@desc:
    55. 跳跃游戏
    给定一个非负整数数组，你最初位于数组的第一个位置。

    数组中的每个元素代表你在该位置可以跳跃的最大长度。

    判断你是否能够到达最后一个位置。

    示例 1:

    输入: [2,3,1,1,4]
    输出: true
    解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
    示例 2:

    输入: [3,2,1,0,4]
    输出: false
    解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

'''

class Solution:
    def __init__(self):
        self.res_list = []
    
    # 回溯法 一：超时
    def canJump1(self, nums):
        def backtrack(p,nums):
            nums_len = len(nums)
            if p == nums_len-1:
                return True
            if (nums[p]+p) <(nums_len):
                jump = nums[p] + p
            else:
                jump = nums_len

            for i in range(jump,p,-1):
                if backtrack(i,nums):
                    return True
            return False 

        return backtrack(0,nums)

    # 回溯法 二：超时
    def canJump2(self, nums):
        nums_len = len(nums) - 1
        if nums_len == 0 and nums[0] == 0:
            return True
        for i in range(1,min(nums[0]+1,nums_len)):
            if  i == nums_len:
                return True
            elif i > nums_len:
                return False
            else:
                flag = self._dfs(nums[i:])
                if flag:
                    return True
        return False

    def _dfs(self,nums):
        nums_len = len(nums) - 1
        if nums_len == 0 and nums[0] == 0:
            return True
        for i in range(1,min(nums[0]+1,nums_len)):
            if  i == nums_len:
                return True
            elif i > nums_len:
                return False
            else:
                flag = self._dfs(nums[i:])
                if flag:
                    return True
        return False

    # 贪心法
    def canJump(self, nums): 
        nums_len = len(nums)
        last = nums_len - 1
        for i in range(last,-1,-1):
            if i + nums[i] >= last:
                last = i
        return not last

if __name__ == "__main__":

    print("--------1-------")
    nums = [2,3,1,1,4]
    solution = Solution()
    res=solution.canJump(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = [3,2,1,0,4]
    solution = Solution()
    res=solution.canJump(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = [0]
    solution = Solution()
    res=solution.canJump(nums)
    print("res:{0}".format(res))

    print("--------4-------")
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    solution = Solution()
    res=solution.canJump(nums)
    print("res:{0}".format(res))
