#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/9 
@desc:
    21. 合并两个有序链表
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：

        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4

'''

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
    工具方法 begin
'''
# 功能：列表转链表
def arr2List(arr_list):
    '''
    列表转链表
    :param arr_list: List  列表
    :return:
        ln_head： ListNode  链表
    '''
    if len(arr_list) > 0:
        ln_head = ListNode(arr_list[0])
        p = ln_head
        for i in range(1, len(arr_list)):
            ln = ListNode(arr_list[i])
            p.next = ln
            p = p.next
        return ln_head
    else:
        return None

# 功能：输出链表
def print_list(ln_head):
    '''
    输出链表
    :param ln_head:  listNode   链表
    :return:

    '''
    print("--------Print List-------")
    i = 0
    while ln_head:
        print("ln[{0}].val:{1}".format(i, ln_head.val))
        ln_head = ln_head.next
        i = i + 1

'''
    工具方法 end
'''

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(-1)
        h = head
        p = l1
        q = l2
        while p and q:
            if p.val < q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        
        return head.next
        
if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    arrs1=[1,2,4]
    arrs2=[1,3,4]
    ln1 = arr2List(arrs1)
    ln2 = arr2List(arrs2)
    res=solution.mergeTwoLists(ln1,ln2)
    print_list(res)


    print("--------2-------")
    arrs1=[]
    arrs2=[1,3,4]
    ln1 = arr2List(arrs1)
    ln2 = arr2List(arrs2)
    res=solution.mergeTwoLists(ln1,ln2)
    print_list(res)

    