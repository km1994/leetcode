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
    
    
'''
while 1:
  g_list = []
  b_list = []
  str1 = input()
  n,m = str1.split(' ')
  n = int(n)
  m = int(m)
  
  str1 = input()
  count = 1
  a = 0
  b = 0
  while count<=n+m:
    if count > 0 and count <= n:
      a,b = str1.split(' ')
      a = int(a)
      b = int(b)
      count = count + 1
      flag = False
      for g in g_list:
        if g[1]>a and g[0]<a and g[1]<b:
          flag = True
          g[1] = b
        elif g[0]>a and g[0]<b and b<g[1]:
          g[0] = a
          flag = True
      if not flag:
        g_list.append([a,b])
    elif count > n and count <= n+m:
      b_list.append(int(str1[0]))
      count = count + 1

    str1 = input()

  del m,n
  count = 0
  a = 0
  b = 0
  b_list = sorted(b_list)
  g_list = sorted(g_list)
  while a < len(b_list) and b < len(g_list):
    if b_list[a] >= g_list[b][0] and b_list[a] <= g_list[b][1]:
      count = count+1
      a = a+1
    else:
      b = b+1

  print(count)
