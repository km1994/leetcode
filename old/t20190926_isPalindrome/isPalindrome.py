#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/26
@url：https://leetcode-cn.com/problems/palindrome-number/
@desc:
    
    9. 回文数

    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

    输入: 121
    输出: true
    示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。


'''
import math
class Solution:
  def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x_len = len(x)
        if x_len<1 or x is None:
            return False
        
        '''
            //接下来的三行是主要的步骤。
            //1.从两头开始比较数字是否一样，如果一样的话就像中间靠拢，如果不一样返回false。
            //2.当左数或者右数任意一个过了中点那么就返回true.
        '''
        left = 0
        right = x_len - 1

        while left>-1 and right <x_len and x[left] == x[right]:
            left += 1
            right -= 1
            if left > int(x_len)/2:
                return True
        return False

if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums = 121
    res=solution.isPalindrome(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = -121
    res=solution.isPalindrome(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = None
    res=solution.isPalindrome(nums)
    print("res:{0}".format(res))
    