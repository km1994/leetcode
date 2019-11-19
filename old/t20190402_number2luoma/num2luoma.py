#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: num2luoma.py
@time: 2019/4/2 19:04
@desc:

    罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

    示例 1:
        输入: 3
        输出: "III"
    示例 2:
        输入: 4
        输出: "IV"
    示例 3:
        输入: 9
        输出: "IX"
    示例 4:
        输入: 58
        输出: "LVIII"
        解释: L = 50, V = 5, III = 3.
    示例 5:
        输入: 1994
        输出: "MCMXCIV"
        解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''
class Solution:
    def intToRoman(self, num):
        luoma=''
        i=0
        # 限制条件，保证整数在[1,3999]内
        if num >=4000 and num <1:
            return ""
        # 用于判断该数是否大于1000，若大于1000 ，则添加 int(num/1000) 个“M”
        if num >= 1000:
            for i in range(0,int(num/1000)):
                luoma = luoma+"M"
                num = num - 1000
        # 判断该数是否大于900，因为大于900时，需要用减法，即添加“CM”
        if num >= 900:
            luoma=luoma+"CM"
            num = num - 900
        # 用于判断该数是否大于500，若大于，则加“D”,并减去500
        if num >=500:
            luoma=luoma+"D"
            num = num -500
        # 判断该数是否大于400，因为大于400时，需要用减法，即添加“CD”
        if num >=400:
            luoma=luoma+"CD"
            num = num -400

        if num >=100:
            for i in range(0,int(num/100)):
                luoma = luoma + "C"
                num = num - 100

        if num >=90:
            luoma = luoma + "XC"
            num = num -90

        if num >=50:
            luoma = luoma+"L"
            num = num -50

        if num >=40:
            luoma = luoma + "XL"
            num = num -40

        if num >=10:
            for i in range(0,int(num/10)):
                luoma = luoma +"X"
                num = num -10

        if num >=9:
            luoma = luoma + "IX"
            num = num - 9

        if num >=5:
            luoma =luoma + "V"
            num = num -5

        if num >=4:
            luoma = luoma+"IV"
            num = num -4

        for i in range(0,num):
            luoma = luoma+"I"

        i=None

        return luoma

if __name__ == "__main__":
    solution=Solution()
    luoma = solution.intToRoman(1400)
    print("luoma:{0}".format(luoma))

