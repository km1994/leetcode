#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/12
@url：https://leetcode-cn.com/problems/unique-binary-search-trees/
@desc:
    
    96. 不同的二叉搜索树

    给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

    示例:

    输入: 3
    输出: 5
    解释:
    给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

'''

class Solution:
  # 方法一：动态规划法
  def numTrees1(self, n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
      for j in range(1,i+1):
        dp[i] = dp[i] + dp[j-1] * dp[i-j]
    
    return dp[n]

  # 方法二：数学演绎法
  def numTrees(self, n):
    C = 1
    for i in range(0,n):
      C = C*2*(2*i+1)/(i+2)
    return int(C)
      

if __name__ == "__main__":
    solution = Solution()
    print("--------1-------")
    nums1 = 3
    res=solution.numTrees(nums1)
    print("res:{0}".format(res))

   