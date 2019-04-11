#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: isValid.py
@time: 2019/4/10 10:56
@desc:
    20. 有效的括号
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

    示例 1:
        输入: "()"
        输出: true
    示例 2:
        输入: "()[]{}"
        输出: true
    示例 3:
        输入: "(]"
        输出: false
    示例 4:
        输入: "([)]"
        输出: false
    示例 5:
        输入: "{[]}"
        输出: true
'''


class Solution:
    def isValid(self, s):
        isValid_list=[]
        for char in s:
            if char == "(":
                isValid_list.append("(")
            elif char == "{":
                isValid_list.append("{")
            elif char == "[":
                isValid_list.append("[")
            elif char == ")":
                if len(isValid_list) == 0:
                    return False
                if isValid_list[-1] == "(":
                    isValid_list.pop()
                else:
                    print("1")
                    return False
            elif char == "}":
                if len(isValid_list) == 0:
                    return False
                if isValid_list[-1] == "{":
                    isValid_list.pop()
                else:
                    print("2")
                    return False
            elif char == "]":
                if len(isValid_list) == 0:
                    return False
                if isValid_list[-1] == "[":
                    isValid_list.pop()
                else:
                    print("3")
                    return False
            else:
                return False

        if len(isValid_list) == 0:
            return True
        else:
            print("4")
            return False

if __name__ == "__main__":
    solution=Solution()
    isValid = solution.isValid("]")
    print("isValid:{0}".format(isValid))
