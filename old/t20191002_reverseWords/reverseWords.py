#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/02
@url：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
@desc:
    
    557. 反转字符串中的单词 III

    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

    示例 1:

    输入: "Let's take LeetCode contest"
    输出: "s'teL ekat edoCteeL tsetnoc" 
    注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

'''
import math
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(" ")
        new_word_list = []
        for word in word_list:
            word = list(word)
            word_len = len(word)
            left = 0
            right = word_len - 1
            while left < right:
                temp = word[left]
                word[left] = word[right]
                word[right] = temp
                left = left + 1
                right = right - 1
            new_word_list.append("".join(word))
        return " ".join(new_word_list)

if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 = "Let's take LeetCode contest"
    res=solution.reverseWords(nums1)
    print("res:{0}".format(res))




    

    