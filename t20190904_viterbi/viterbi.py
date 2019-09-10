#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/04
@url：
@desc:
    
    维特比算法

'''
states = ('健康','感冒')  # 状态变量
observations = ('正常','发冷','发烧') # 观测变量

start_probability = {'健康':0.6,'感冒':0.4}  # 初始状态

transition_probability = {  # 状态转移矩阵
  '健康':{'健康':0.7, '感冒':0.3},
  '感冒':{'健康':0.4, '感冒':0.6}
}

emission_probability = {   # 观测概率矩阵
  '健康':{'正常':0.5, '发冷':0.4, '发烧':0.1},
  '感冒':{'正常':0.1, '发冷':0.3, '发烧':0.6}
}

def viterbi(obs,states,start_p,trans_p,emit_p):
  V =[{}]
  path = {}
  for y in states:  # 建立 t_0 时刻各状态的概率 
    V[0][y] = start_p[y] * emit_p[y][obs[0]]
    path[y] = [y]

  for t in range(1,len(obs)):   # 沿着时间(1,2,..,t) 进行计算
    V.append({})
    newpath = {}

    # 根据 t-1 时刻状态概率、观测概率矩阵和状态转移概率
    # 计算 t 时刻最大概率的状态，记录路径
    for y in states:
      (prob,state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]],y0) for y0 in states])
      V[t][y] = prob
      newpath[y] = path[state] + [y]

    path = newpath

  (prob,state) = max([(V[len(obs)-1][y],y) for y in states])
  return (prob,path[state])

res = viterbi(observations,states,start_probability,transition_probability,emission_probability)
print("res:{0}".format(res))
