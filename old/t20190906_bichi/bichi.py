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
    
  有一个数组每次只能两边取值，小红和小明竞赛，
  轮流取值，小红先取，获胜的可能是多少


'''
while 1:
  a=[]  
  str1 = input()
  if str1 != "":
    arr = [int(s) for s in str1.split(" ")]
    xiaomi = 0
    dami = 0 
    if arr[0] > arr[-1]:
      for i in range(0,len(arr),2):
        xiaomi = xiaomi + arr[i]
      
      for i in range(1,len(arr),2):
        dami = dami + arr[i]
    else:
      for i in range(len(arr)-1,-1,-2):
        xiaomi = xiaomi + arr[i]
      
      for i in range(len(arr)-2,-1,-2):
        dami = dami + arr[i]
    if xiaomi >= dami:
      print(True)
    else:
      print(False)

  else:
    break