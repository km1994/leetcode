#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: isValid.py
@time: 2019/4/15 11:56
@desc:
    22. 括号生成
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

    例如，给出 n = 3，生成结果为：

        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
'''


class Solution:
    def __init__(self):
        self.parenthesis_list=[]
    def generateParenthesis1(self, n):
        parenthesis_str="("
        l=1
        r=0
        self.generateLeftParenthesis( parenthesis_str, l, r, n)
        self.generateRightParenthesis( parenthesis_str, l, r, n)

        return self.parenthesis_list

    # 功能：生成左括号
    def generateLeftParenthesis(self, parenthesis_str,l,r,n):
        '''
        功能：生成左括号
        :param parenthesis_str: 存储括号字符串
        :param l:  左括号个数
        :param r:  右括号个数
        :param n:  需要生成的括号数目
        :return:

        '''
        # 当字符串中左括号的数量少于所需要的括号数时，可以再补充左括号
        # 然后进行往下左右递归
        if l<n:
            parenthesis_str = parenthesis_str + "("
            l = l+1
            self.generateLeftParenthesis( parenthesis_str, l, r, n)
            self.generateRightParenthesis( parenthesis_str, l, r, n)
        # 当字符串中左括号的数量等于所需要的括号数时，可以再补充(l-r)右括号
        elif l == n:
            parenthesis_str = parenthesis_str + ")"*(l-r)
            self.parenthesis_list.append(parenthesis_str)
        # 表示所需括号为 0 个，此时需要返回“”
        else:
            self.parenthesis_list.append("")

    # 功能：生成右括号
    def generateRightParenthesis(self, parenthesis_str,l,r,n):
        '''
        功能：生成右括号
        :param parenthesis_str: 存储括号字符串
        :param l:  左括号个数
        :param r:  右括号个数
        :param n:  需要生成的括号数目
        :return:

        '''
        # 当字符串中左括号的数量少于所需要的括号数时，且大于右括号数目加一时，可以再补充右括号
        # 然后进行往下左右递归
        if l<n and l>=r+1:
            parenthesis_str = parenthesis_str + ")"
            r = r + 1
            self.generateLeftParenthesis( parenthesis_str, l, r, n)
            self.generateRightParenthesis( parenthesis_str, l, r, n)

if __name__ == "__main__":
    solution=Solution()
    res = solution.generateParenthesis(0)
    print("res:{0}".format(res))


