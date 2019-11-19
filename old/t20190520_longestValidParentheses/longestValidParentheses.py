#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/5/20
@rel： https://leetcode-cn.com/problems/longest-valid-parentheses/
@url：
@desc:
    32. 最长有效括号
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
    示例 1:
        输入: "(()"
        输出: 2
        解释: 最长有效括号子串为 "()"
    示例 2:
        输入: ")()())"
        输出: 4
        解释: 最长有效括号子串为 "()()"

'''


class Solution:
    def __init__(self):
        pass

    def  longestValidParentheses(self, s) :
        st, b = [], [0] * len(s)
        for i, val in enumerate(s):
            if val == '(':
                st.append(i)
            elif st:
                b[st.pop()], b[i] = 1, 1

        print("st:{0}".format(st))
        print("b:{0}".format(b))
        c, mc = 0, 0
        for i in b:
            if i:
                c += 1
            else:
                mc = max(c, mc)
                c = 0

        return max(c, mc)



if __name__ == "__main__":
    parentheses1='(()()'
    solution = Solution()
    res1 = solution.longestValidParentheses(parentheses1)
    print("res1:{0}".format(res1))

    parentheses2 = ')()())'
    res2 = solution.longestValidParentheses(parentheses2)
    print("res2:{0}".format(res2))

    parentheses3 = '(()())'
    res3 = solution.longestValidParentheses(parentheses3)
    print("res3:{0}".format(res3))

    parentheses4 = "()(()"
    res4 = solution.longestValidParentheses(parentheses4)
    print("res4:{0}".format(res4))


