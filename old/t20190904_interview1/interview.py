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
    
    样例输入
10
1 0.90
0 0.70
1 0.60
1 0.55
0 0.52
1 0.40
0 0.38
0 0.35
1 0.31
0 0.10
样例输出
0.68

'''
def calAUC(prob,labels):
    f = list(zip(prob,labels))
    rank = [values2 for values1,values2 in sorted(f,key=lambda x:x[0])]
    rankList = [i+1 for i in range(len(rank)) if rank[i]==1]
    posNum = 0
    negNum = 0
    for i in range(len(labels)):
        if(labels[i]==1):
            posNum+=1
        else:
            negNum+=1
    auc = 0
    auc = (sum(rankList)- (posNum*(posNum+1))/2)/(posNum*negNum)
    return auc


while 1:
  true_list = []
  pred_list = []
  num = 0
  flag = True
  str1 = input()
  while str1 != '':
    if flag and ' ' not in str1:
      flag = False
      num = int(str1)
    elif ' ' in str1:
      a,b = str1.split(' ')
      true_list.append(float(a))
      pred_list.append(float(b))
	
    str1 = input()
    
      
  auc = calAUC(pred_list,true_list)
  print(auc)