#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/25
@url：https://leetcode-cn.com/problems/plus-one/
@desc:
    66. 加一
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

    最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

    你可以假设除了整数 0 之外，这个整数不会以零开头。

    示例 1:

    输入: [1,2,3]
    输出: [1,2,4]
    解释: 输入数组表示数字 123。
    示例 2:

    输入: [4,3,2,1]
    输出: [4,3,2,2]
    解释: 输入数组表示数字 4321。

'''

class Solution:
    def plusOne(self, digits):
        digits_len = len(digits)
        yushu = int((digits[-1] + 1)/10)
        digits[-1] = (digits[-1] + 1)%10
        pos = 2
        while yushu:
            if pos <= digits_len:
                yushu = int((digits[digits_len - pos] + 1)/10)
                digits[digits_len - pos] = (digits[digits_len - pos] + 1)%10
                pos += 1
            else:
                digits.append(0)
                digits[0] = 1
                yushu = 0
        return digits



if __name__ == "__main__":

    print("--------1-------")
    nums = [1,2,3]
    solution = Solution()
    res=solution.plusOne(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = [4,3,2,1]
    solution = Solution()
    res=solution.plusOne(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = [9]
    solution = Solution()
    res=solution.plusOne(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = [9,9,9]
    solution = Solution()
    res=solution.plusOne(nums)
    print("res:{0}".format(res))

    print("--------4-------")
    nums = [8,9,9]
    solution = Solution()
    res=solution.plusOne(nums)
    print("res:{0}".format(res))