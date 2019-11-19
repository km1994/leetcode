#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/25
@url：https://leetcode-cn.com/classic/problems/nim-game/description/
@desc:
    292. Nim 游戏
    
    你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

    你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。

    示例:

    输入: 4
    输出: false 
    解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
        因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。

'''

class Solution:
    def canWinNim(self, n):
        if n%4 != 0:
            return True
        else:
            return False



if __name__ == "__main__":

    print("--------1-------")
    nums = 4
    solution = Solution()
    res=solution.canWinNim(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = 11
    solution = Solution()
    res=solution.canWinNim(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = 9
    solution = Solution()
    res=solution.canWinNim(nums)
    print("res:{0}".format(res))

    print("--------4-------")
    nums = 100
    solution = Solution()
    res=solution.canWinNim(nums)
    print("res:{0}".format(res))

    print("--------5-------")
    nums = 111
    solution = Solution()
    res=solution.canWinNim(nums)
    print("res:{0}".format(res))