#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/9 
@desc:
    30. 串联所有单词的子串
    给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

    注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

    示例 1：

    输入：
    s = "barfoothefoobarman",
    words = ["foo","bar"]
    输出：[0,9]
    解释：
    从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
    输出的顺序不重要, [9,0] 也是有效答案。
    示例 2：

    输入：
    s = "wordgoodgoodgoodbestword",
    words = ["word","good","best","word"]
    输出：[]


'''

class Solution:
    def findSubstring(self, s, words):
        res = []
        s_len = len(list(s))
        words_num = len(words)
        if words_num == 0:
            return []
        
        word_len = len(words[0])

        # 利用 HashMap1 存储所有单词
        words_all_dict = {}
        for word in words:
            if word not in words_all_dict:
                words_all_dict[word] = 1
            else:
                words_all_dict[word] += 1

        # 遍历所有子串
        for i in range(s_len - word_len*words_num+1):
            # 利用 HashMap2存储当前扫描的字符串含有的单词
            has_words_dict = {}
            num = 0
            while num < words_num:
                # 判断该单词是否在 words_all_dict 中
                s_word = s[i+num*word_len:i+(num+1)*word_len]
                if s_word in words_all_dict:
                    if s_word not in has_words_dict:
                        has_words_dict[s_word] = 1
                    else:
                        has_words_dict[s_word] += 1
                    
                    if has_words_dict[s_word]>words_all_dict[s_word]:
                        break
                else:
                    break
                num += 1
            if num == words_num:
                res.append(i)
        return res


if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    res=solution.findSubstring(s,words)
    print(res)



    