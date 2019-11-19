#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: strStr.py
@time: 2019/6/23
@rel： https://leetcode-cn.com/problems/implement-strstr/
@url：
@desc:
    28. 实现 strStr()
    实现 strStr() 函数。

    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

    示例 1:

    输入: haystack = "hello", needle = "ll"
    输出: 2
    示例 2:

    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
    说明:

    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/implement-strstr
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def __init__(self):
        pass

    def strStr(self, haystack, needle):
        len_a = len(haystack)
        len_b = len(needle)

        if  haystack == needle:
            return 0

        for i in range(0,(len_a-len_b+1)):
            if haystack[i:i+len_b] == needle:
                return i

        return -1



if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    solution = Solution()
    res = solution.strStr(haystack,needle)
    print("res:{0}".format(res))

    haystack = "aaaaa"
    needle = "bba"
    res = solution.strStr(haystack, needle)
    print("res:{0}".format(res))

    haystack = ""
    needle = ""
    res = solution.strStr(haystack, needle)
    print("res:{0}".format(res))

    haystack = "a"
    needle = "a"
    res = solution.strStr(haystack, needle)
    print("res:{0}".format(res))
    

