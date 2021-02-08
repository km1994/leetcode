#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/04
@url：https://leetcode-cn.com/problems/n-queens/
@desc:
    
    234. 回文链表

    请判断一个链表是否为回文链表。

      示例 1:	

        输入: 1->2
        输出: false
      
      示例 2:

        输入: 1->2->2->1
        输出: true

'''
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 数组 -> 链表
def arr2list(arr):
  head = ListNode(-1)
  p = head
  for num in arr:
    node = ListNode(num)
    p.next = node
    p = p.next
  p.next = None
  return head

# 打印链表
def displayList(head):
  if not head:
    return 
  p = head
  while p:
    print(p.val)
    p = p.next


class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		head_len = 0
		p = head
		while p:
			head_len = head_len+1
			p = p.next
		mid = math.floor(head_len/2)
		qHead = ListNode(0)
		p = head
		q = qHead
		while mid>0:
			tmp = q.next
			q.next = p
			p = p.next
			q.next.next = tmp
			mid = mid - 1
		if head_len%2==1:
			p = p.next
		q = qHead.next
		while p and q:
			if p.val != q.val:
				return False
			p=p.next
			q=q.next
		return True

#   def isPalindrome1(self, head):
    
#     pre_head = ListNode(-1)
#     pre_head.next = head
#     head = pre_head

#     list_len = 0
#     p = head.next
#     while p:
#       list_len = list_len + 1
#       p = p.next
    
#     flag = True
#     temp_head = ListNode(-1)
#     tail = temp_head.next 
#     p = head.next
#     if list_len%2  == 1:
#       print("--1--")
#       for i in range(0,int(list_len/2)):
#         temp_head.next = p
#         p = p.next
#         temp_head.next.next = tail
#         tail = temp_head.next
      
#       p = p.next
#       while p and tail and p.val == tail.val:
#         p = p.next
#         tail = tail.next
      
#       if p or tail:
#         return False
#       else:
#         return True
#     else:
#       print("--2--")
#       for i in range(0,int(list_len/2)):
#         temp_head.next = p
#         p = p.next
#         temp_head.next.next = tail
#         tail = temp_head.next

#       while p and tail and p.val == tail.val:
#         p = p.next
#         tail = tail.next
      
#       if p or tail:
#         return False
#       else:
#         return True
  
#   def isPalindrome2(self, head):
#       list_len = 0
#       p = head
#       while p:
#           list_len = list_len + 1
#           p = p.next
      
#       temp_head = ListNode(-1)
#       tail = temp_head.next 
#       p = head
#       for i in range(0,int(list_len/2)):
#           temp_head.next = p
#           p = p.next
#           temp_head.next.next = tail
#           tail = temp_head.next

#       p = p.next if list_len%2  == 1 else p
      
#       while p and tail and p.val == tail.val:
#           p = p.next
#           tail = tail.next

#       return False if p or tail else True
    

  
if __name__ == "__main__":

    print("--------1-------")
    arr = [1,2]
    head = arr2list(arr)
    displayList(head.next)
    solution = Solution()
    res=solution.isPalindrome(head.next)
    print("res:{0}".format(res))

    print("--------2-------")
    arr = [1,2,2,2,1]
    head = arr2list(arr)
    displayList(head.next)
    solution = Solution()
    res=solution.isPalindrome(head.next)
    print("res:{0}".format(res))

    print("--------3-------")
    arr = [1,2,2,2,4]
    head = arr2list(arr)
    displayList(head.next)
    solution = Solution()
    res=solution.isPalindrome(head.next)
    print("res:{0}".format(res))

    print("--------4-------")
    arr = []
    head = arr2list(arr)
    displayList(head.next)
    solution = Solution()
    res=solution.isPalindrome(head.next)
    print("res:{0}".format(res))

    