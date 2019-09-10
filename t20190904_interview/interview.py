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
    
    时刻表内容：aabbcddc，a,b,c,d为目的地，字母出现的先后顺序为出发时间的先后顺序
    样例输入
      aabbcddc
    样例输出
      2,2,4
'''
while 1:
  a= []
  str1 = input()
  count = 0
  count_list = []
  for char in str1:
    if len(a) == 0:
      a.append(char)
      count = count + 1
    elif char == a[-1]:
      count = count + 1
      count_list.append(str(count))
      a.pop()
      count = 0
    else:
      count = count + 1

  print(",".join(count_list))





  