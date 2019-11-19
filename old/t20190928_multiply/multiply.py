#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/28
@url：https://leetcode-cn.com/problems/multiply-strings/submissions/
@desc:
    
    43. 字符串相乘

    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

    示例 1:

    输入: num1 = "2", num2 = "3"
    输出: "6"
    示例 2:

    输入: num1 = "123", num2 = "456"
    输出: "56088"
    说明：

    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

'''
import math
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)
        
        return str(num1*num2)
  

if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 = "2"
    nums2 = "3"
    res=solution.multiply(nums1,nums2)
    print("res:{0}".format(res))

    