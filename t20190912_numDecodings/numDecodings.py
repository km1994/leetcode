#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/12
@url：https://leetcode-cn.com/problems/decode-ways/
@desc:
    
    121. 买卖股票的最佳时机

    一条包含字母 A-Z 的消息通过以下方式进行了编码：

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
      给定一个只包含数字的非空字符串，请计算解码方法的总数。

      示例 1:
        输入: "12"
        输出: 2
        解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
      示例 2:
        输入: "226"
        输出: 3
        解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

'''

class Solution:
  def __init__(self):
    int2char_list = [
        '0',"A",'B',"C",'D',"E",'F',"G",
        'H',"I",'J',"K",'L',"M",'N',
        'O',"P",'Q',"R",'S',"T",
        "U",'V',"W",'X','Y',"Z"
      ]
    

  def numDecodings(self, s):
    def help(i):
      if i in dic:
        return dic[i]
      if i >= len(s):
        return 1
      
      res = 0
      # 第一位合法情况（0 不合法）
      if 1 <= int(s[i]) <= 9:
        res = res + help(i+1)

      # 前两位合法的情况
      if 10 <= int(s[i:i+2]) <= 26:
        res = res + help(i+2)
      
      # 之所以需要dic, 是因为i + 1, i + 2的两次递归调用, 会产生重复计算
      dic[i] = res
      return res
    
    dic = {}
    return help(0) if s else 0
      

if __name__ == "__main__":
    solution = Solution()
    print("--------1-------")
    nums1 = '12'
    res=solution.numDecodings(nums1)
    print("res:{0}".format(res))

    print("--------2-------")
    nums1 = '026'
    res=solution.numDecodings(nums1)
    print("res:{0}".format(res))

    print("--------3-------")
    nums1 = '0'
    res=solution.numDecodings(nums1)
    print("res:{0}".format(res))

    print("--------4-------")
    nums1 = '326'
    res=solution.numDecodings(nums1)
    print("res:{0}".format(res))

    print("--------5-------")
    nums1 = '10'
    res=solution.numDecodings(nums1)
    print("res:{0}".format(res))

    print("--------6-------")
    nums1 = '27'
    res=solution.numDecodings(nums1)
    print("res:{0}".format(res))




   