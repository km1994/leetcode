#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: MinStack.py
@time: 2019/8/03
@rel： https://leetcode-cn.com/problems/min-stack/
@url：
@desc:
    44. 通配符匹配

    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    两个字符串完全匹配才算匹配成功。

    说明:

    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
    示例 1:
        输入:
        s = "aa"
        p = "a"
        输出: false
        解释: "a" 无法匹配 "aa" 整个字符串。
    示例 2:
        输入:
        s = "aa"
        p = "*"
        输出: true
        解释: '*' 可以匹配任意字符串。
    示例 3:
        输入:
        s = "cb"
        p = "?a"
        输出: false
        解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
    示例 4:
        输入:
        s = "adceb"
        p = "*a*b"
        输出: true
        解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
    示例 5:
        输入:
        s = "acdcb"
        p = "a*c?b"
        输入: false
'''

class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

        def isMatch(self, s, p):
            i=0
            j=0
            s_lem = len(s)
            p_len = len(p)
            while i < len(s) and j < len(p):
                if p[j] == '?':
                    i = i + 1
                    j = j + 1
                elif p[j] == '*':
                    if s_lem > i+1 :
                        if




if __name__ == "__main__":
    s = "aa"
    p = "a"
    solution =Solution()




