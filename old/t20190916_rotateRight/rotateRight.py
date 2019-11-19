#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/9/16 
@desc:
    61. 旋转链表
    给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

    示例 1:

        输入: 1->2->3->4->5->NULL, k = 2
        输出: 4->5->1->2->3->NULL
        解释:
        向右旋转 1 步: 5->1->2->3->4->NULL
        向右旋转 2 步: 4->5->1->2->3->NULL
    示例 2:

        输入: 0->1->2->NULL, k = 4
        输出: 2->0->1->NULL
        解释:
        向右旋转 1 步: 2->0->1->NULL
        向右旋转 2 步: 1->2->0->NULL
        向右旋转 3 步: 0->1->2->NULL
        向右旋转 4 步: 2->0->1->NULL

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
    def rotateRight(self, head, k):
        if not head:
            return head
        pre_head = ListNode(-1)
        pre_head.next = head

        head_len = 0
        p = pre_head.next
        while p:
            head_len = head_len + 1
            p = p.next

        k = k%head_len

        p = pre_head.next
        i = 0
        while i < k and p.next:
            p = p.next
            i = i + 1

        q = pre_head.next
        while p.next:
            p = p.next
            q = q.next
        
        p.next = pre_head.next
        pre_head.next = q.next
        q.next = None
        
        return pre_head.next

        
if __name__ == "__main__":
    
    solution = Solution()

    print("--------1-------")
    arrs1=[1,2,3,4,5]
    k = 2
    ln1 = arr2List(arrs1)
    res=solution.rotateRight(ln1,k)
    print_list(res)

    print("--------2-------")
    arrs1=[0,1,2]
    k = 4
    ln1 = arr2List(arrs1)
    res=solution.rotateRight(ln1,k)
    print_list(res)

    print("--------3-------")
    arrs1=[1,2]
    k = 1
    ln1 = arr2List(arrs1)
    res=solution.rotateRight(ln1,k)
    print_list(res)




    