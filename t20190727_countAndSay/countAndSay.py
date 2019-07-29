#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: generateMatrix.py
@time: 2019/7/24
@rel： https://leetcode-cn.com/problems/spiral-matrix-ii/
@url：
@desc:
    42. 接雨水


'''
class Solution:
    def __init__(self):
        pass

    def countAndSay(self, n):
        sayStr =''
        if n == 0:
            return sayStr

        sayStr = '1'
        print(sayStr[0])
        for i in range(2,n+1):
            temp = ''
            nowChar = sayStr[0]
            nowCount = 1
            for j in range(1,len(sayStr)):
                if nowChar == sayStr[j]:
                    nowCount = nowCount + 1
                else:
                    temp = temp + str(nowCount) + nowChar
                    nowChar = sayStr[j]
                    nowCount = 1

            temp = temp + str(nowCount) + nowChar
            sayStr=temp

        return str(sayStr)


if __name__ == "__main__":

    solution = Solution()

    n = 1
    res1 = solution.countAndSay(n)
    print("res1:{0}".format(res1))

    n = 2
    res1 = solution.countAndSay(n)
    print("res2:{0}".format(res1))

    n = 3
    res1 = solution.countAndSay(n)
    print("res3:{0}".format(res1))

    n = 4
    res1 = solution.countAndSay(n)
    print("res4:{0}".format(res1))

    n = 5
    res1 = solution.countAndSay(n)
    print("res5:{0}".format(res1))






    

