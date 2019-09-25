#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/18
@url：https://leetcode-cn.com/problems/sqrtx/
@desc:
    
    69. x 的平方根

    实现 int sqrt(int x) 函数。

    计算并返回 x 的平方根，其中 x 是非负整数。

    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

    示例 1:
      输入: 4
      输出: 2
    示例 2:
      输入: 8
      输出: 2
    说明: 8 的平方根是 2.82842..., 
         由于返回类型是整数，小数部分将被舍去。

'''
class Solution:
  '''
  # 二分法
  
  '''
  def mySqrt1(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
      return 0

    left = 1
    right = x//2

    while left<right:
      mid = (left+right+1)>>1
      square = mid * mid
      if square>x:
        right = mid-1
      else:
        left = mid
    return left

  '''
  # 牛顿法
  
  '''
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
      return 0
    cur = 1
    while True:
      pre = cur
      cur = (cur+x/cur)/2
      if abs(cur-pre) < 1e-6:
        return int(cur)


if __name__ == "__main__":

    print("--------1-------")

    nums = 4
    solution = Solution()
    res=solution.mySqrt(nums)
    print("res:{0}".format(res))

    