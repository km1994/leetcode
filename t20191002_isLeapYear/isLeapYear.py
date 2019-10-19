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
    
    

'''

def is_leap_year(year):
    print(year%4==0)
    print(year%100!=0)
    print(year%400==0)
    print("year%4==0 and year%100!=0 or year%400==0:{0}".format(year%4==0 and year%100!=0 or year%400==0))
    return year%4==0 and year%100!=0 or year%400==0

if __name__ == "__main__":
    year = 1004
    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31],
        [31,30,31,30,31,30,31,31,30,31,30,31],
        [31,31,31,30,31,30,31,31,30,31,30,31]
    ][3]

    print(days_of_month)

    


    

    