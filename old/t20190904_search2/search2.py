#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/04
@url：
@desc:
    
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。

  ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

  编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

  示例 1:

  输入: nums = [2,5,6,0,0,1,2], target = 0
  输出: true
  示例 2:

  输入: nums = [2,5,6,0,0,1,2], target = 3
  输出: false



'''
class Solution:

    def search(self, nums, target):
        if not nums:
            return False
          
        temp_list = []
        for num in nums:
          if num not in temp_list:
            temp_list.append(num)
        nums = temp_list


        if nums[0] == target:
            return True

        for i in range(1,len(nums)):
          if nums[i] != target and nums[i-1] > nums[i]:
            if self.Bisectionmethod(nums, target, 0, i-1) or self.Bisectionmethod(nums, target, i, len(nums)):
              return True
          elif nums[i] == target:
            return True
        return False

    def Bisectionmethod(self, nums, target, l, r):
      mid = l + (r - l) // 2
      while l <= r:
        mid = l + (r - l) // 2
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
        if nums[mid] == target:
            return True
        else:
            return False



if __name__ == "__main__":

    print("--------1-------")
    nums = [2,5,6,0,0,1,2]
    target = 0
    solution = Solution()
    res=solution.search(nums, target)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = [2,5,6,0,0,1,2]
    target = 3
    solution = Solution()
    res=solution.search(nums, target)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = [1]
    target = 0
    solution = Solution()
    res=solution.search(nums, target)
    print("res:{0}".format(res))

    print("--------4-------")
    nums = [1,3,5]
    target = 1
    solution = Solution()
    res=solution.search(nums, target)
    print("res:{0}".format(res))


    