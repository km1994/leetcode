#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: 
@time: 2019/8/05
@rel： 
@url：
@desc:
    快排

'''

class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

   
    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] < key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] >= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)



if __name__ == "__main__":
    # nums = [3,2,1,5,6,4]
    # k = 2
    # solution =Solution()
    # solution.findKthLargest(nums,k)

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    solution = Solution()
    solution.quick_sort(nums, 0,len(nums)-1)

    print("nums:{0}".format(nums))





