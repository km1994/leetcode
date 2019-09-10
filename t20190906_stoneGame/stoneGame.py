#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/04
@url：https://leetcode-cn.com/problems/n-queens/
@desc:
    
    877. 石子游戏

    亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
    游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
    亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
    假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

    示例：

    输入：[5,3,4,5]
    输出：true
    解释：
    亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
    假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
    如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
    如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
    这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。

'''

class Solution:

  def stoneGame(self, piles):
    return True

  def stoneGame1(self, piles):
    xiaomi = 0
    dami = 0 
    if piles[0] > piles[-1]:
      for i in range(0,len(piles),2):
        xiaomi = xiaomi + piles[i]
      
      for i in range(1,len(piles),2):
        dami = dami + piles[i]
    elif piles[0] < piles[-1]:
      for i in range(len(piles)-1,-1,-2):
        xiaomi = xiaomi + piles[i]
      
      for i in range(len(piles)-2,-1,-2):
        dami = dami + piles[i]
    elif piles[0] == piles[-1]:
      for i in range(0,len(piles),2):
        xiaomi = xiaomi + piles[i]
      
      for i in range(1,len(piles),2):
        dami = dami + piles[i]
      
    if xiaomi > dami:
      return True
    else:
      return False

  
if __name__ == "__main__":

    solution = Solution()
    print("--------1-------")
    nums = [1,2,2,1]
    res=solution.stoneGame(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = [1,2,2,2,1]
    res=solution.stoneGame(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = [5,3,4,5]
    res=solution.stoneGame(nums)
    print("res:{0}".format(res))



    