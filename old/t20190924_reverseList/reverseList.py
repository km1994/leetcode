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
    206. 反转链表
    反转一个单链表。

    示例:

        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL

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
    def reverseList(self, head):
        new_head = ListNode(-1)
        p = head
        q = new_head
        while p:
            temp = q.next
            q.next = p
            p = p.next
            q.next.next = temp

        return new_head.next
        
if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    arrs1=[1,2,4]
    ln1 = arr2List(arrs1)
    res=solution.reverseList(ln1)
    print_list(res)



    