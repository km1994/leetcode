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
    17. 电话号码的字母组合
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    示例:
        输入："23"
        输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution:
    def letterCombinations(self, digits):
        num2char_dict={
            "2":"abc","3":"def","4":"ghi",
            "5":"jkl","6":"mno","7":"pqrs",
            "8":"tuv","9":"wxyz"
        }
        temp=['']
        for d in digits:
            ans=[]
            for char in temp:
                for new_char in num2char_dict[d]:
                    ans.append(char+new_char)
            temp = ans

        print("temp:{0}".format(temp))
        print("len(temp):{0}".format(len(temp)))
        return ans


if __name__ == "__main__":
    solution=Solution()
    solution.letterCombinations("234")


