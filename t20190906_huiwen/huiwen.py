#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/06
@url：https://leetcode-cn.com/problems/add-binary/
@desc:
    
    请判断一个链表是否为回文链表

  输入: 1->2->2->1 输出: True

  输入
  数组

  输出
  True 或者 False


  样例输入
  1 2 2 1
  样例输出
  True

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def arr2list(arr):
  head = ListNode(-1)
  p = head
  for num in arr:
    node = ListNode(num)
    p.next = node
    p = p.next
  p.next = None
  return head

def displayList(head):
  if not head:
    return 
  p = head
  while p:
    print(p.val)
    p = p.next



while 1:
  a=[]  
  str1 = input()
  if str1 != "":
    arr = [int(s) for s in str1.split(" ")]
    if len(arr) == 1:
      print(True)


    head = arr2list(arr)
    #displayList(head)

    temp_head = ListNode(-1)
    tail = ListNode(head.next.val)
    tail.next = None

    temp_head.next = tail

    p = head.next.next
    while p and p.val != tail.val and p.next and p.next.val != tail.val:
      temp_head.next = p
      p = p.next
      temp_head.next.next = tail
      tail = temp_head.next
    
    if p:
      if p.val == tail.val:
        while p and tail and p.val == tail.val:
          p = p.next
          tail = tail.next
      elif p.next and tail and p.next.val == tail.val:
        p = p.next
        while p and tail and p.val == tail.val:
          p = p.next
          tail = tail.next

      if p or tail:
        print(False)
      else:
        print(True)
    else:
      print(False)

  else:
    break

