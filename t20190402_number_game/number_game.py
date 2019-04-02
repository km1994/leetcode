#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: number_game.py
@time: 2019/4/2 11:51
@desc:  有个数，除2余1，除3余0，除4余1，除5少1，除6余3，
        除7余0，除8余1，除9余0，求满足条件最小的数是多少，分
        享求解思路并编程实现。
'''

for i in range(0,2000):
    if (i+1)%5 ==0 and i%8==1 and i%63==0:
        print("num = {0}".format(i))


for i in range(0,2000,63):
    if i%8==1 and (i+1)%5==0:
        print("num = {0}".format(i))


'''



'''
