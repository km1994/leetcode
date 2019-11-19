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
    24. 两两交换链表中的节点
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
        
        示例:

        给定 1->2->3->4, 你应该返回 2->1->4->3.


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
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        prehead = ListNode(-1)
        prehead.next = head
        p = prehead

        while p.next and p.next.next:
            t1 = p.next
            t2 = p.next.next.next
            p.next = t1.next
            t1.next = t2
            p.next.next = t1
            p =t1

        return prehead.next
     
if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    arrs=[1,2,3,4]
    ln = arr2List(arrs)
    print_list(ln)
    res=solution.swapPairs(ln)
    print_list(res)



    