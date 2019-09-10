#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/09
@url：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
@desc:
    
    82. 删除排序链表中的重复元素 II

    给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

    示例 1:
      输入: 1->2->3->3->4->4->5
      输出: 1->2->5
    示例 2:
      输入: 1->1->1->2->3
      输出: 2->3

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
  print("-----dispaly begin------")
  if not head:
    return 
  p = head
  while p:
    print(p.val)
    p = p.next
  print("-----dispaly end------")


class Solution:
  def deleteDuplicates(self, head):
    if not head:
      return head
    pre_head = ListNode(-1)
    pre_head.next = head
    p = pre_head
    q = pre_head.next

    flag = False
    while p.next and q.next:
      if not flag and p.next.val != q.next.val:
        p = p.next
        q = q.next
      elif p.next.val == q.next.val:
        flag = True
        q = q.next
      elif flag and p.next.val != q.next.val:
        flag = False
        q = q.next
        p.next = q
    
    if flag:
      p.next = q.next

    return pre_head.next

if __name__ == "__main__":

    solution = Solution()
    print("--------1-------")
    nums1 = [1,2,3,3,4,4,5]
    head = arr2list(nums1)
    displayList(head.next)

    res=solution.deleteDuplicates(head.next)
    displayList(res)


    print("--------2-------")
    nums1 = [1,1]
    head = arr2list(nums1)
    displayList(head.next)

    res=solution.deleteDuplicates(head.next)
    displayList(res)

   