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
  str1 = input()
  if not str1:
      print(0)
  str1_len = len(str1.split(' '))
  if str1_len < 5:
    print(0) 
  nums,n = str1.split(' ')[0:4],int(str1.split(' ')[-1])
  nums = [int(num) for num in nums]
  for i in range(4,n):
    temp = nums[i-1] + nums[i-3] + nums[i-4]
    nums.append(temp)
  print((nums[-1])%(10**9+7))
  





  