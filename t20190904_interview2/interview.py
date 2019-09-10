#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/31
@url：http://oj.acmcoder.com/ExamNotice.html
@desc:
    
    题目描述：
给定一个非空字符串（只包含小写英文字母，长度不超过1000），判断其是否可以通过自身子串重复若干次构成。

要求：利用KMP算法进行解题。

输入
测试用例有多行数据，对于每行：

是一个长度大于1的字符串，长度不超过1000。

输出
对于每一个字符串，输出一行True or False，判断当前字符串是否可以通过自身子串重复若干次构成。


样例输入
abdabcabdab
abdabcabdabc
样例输出
False
True

'''
while 1:
  a=[]  
  s = input()
  
  if s != "":
    all_str=''
    temp_str=''
    i = 0
    for char in s:
      if len(all_str)==0:
        all_str = all_str + char
      elif len(all_str) > i and all_str[i] != char and len(temp_str) == 0:
        all_str = all_str + char
      elif len(all_str) > i and all_str[i] != char and len(temp_str) != 0:
        all_str = all_str + temp_str + char
        temp_str = ''
        i = 0
      elif len(all_str) > i and all_str[i] == char:
        temp_str = temp_str + char
        i = i + 1
      elif len(all_str) == i:
        temp_str = ''
        i = 0

    if all_str == temp_str:
      print(True)
    else:
      print(False)
  else:
    break