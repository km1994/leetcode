#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@url: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/comments/
@time: 2019/8/9 
@desc:
    25. K 个一组翻转链表
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

    k 是一个正整数，它的值小于或等于链表的长度。

    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    示例 :

    给定这个链表：1->2->3->4->5

    当 k = 2 时，应当返回: 2->1->4->3->5

    当 k = 3 时，应当返回: 3->2->1->4->5

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
    def reverseKGroup(self, head, k):
        cur = head
        check = head
        canProceed = 0
        count = 0
        prev = None
        next =None
        while canProceed < k and check is not None:
            check = check.next
            canProceed = canProceed + 1
        if canProceed == k:
            while count < k and cur is not None:
                next =cur.next
                cur.next = prev
                prev = cur
                cur = next
                count = count + 1
            if next is not None:
                head.next = self.reverseKGroup(next,k)
            return prev
        else:
            return head

            


     
if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    arrs=[1,2,3,4]
    ln = arr2List(arrs)
    k=2
    print_list(ln)
    res=solution.reverseKGroup(ln,k)
    print_list(res)



    