#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@desc:
    160. 相交链表
    编写一个程序，找到两个单链表相交的起始节点。

    如下面的两个链表：
    节点 c1 开始相交。

    示例 1：
        输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
        输出：Reference of the node with value = 8
        输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
         
    示例 2：
        输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
        输出：Reference of the node with value = 2
        输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
     
    示例 3：
        输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
        输出：null
        输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
        解释：这两个链表不相交，因此返回 null。

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
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        a_dict = {}
        i = 0
        while a:
            if a not in a_dict:
               a_dict[a] = i
               i = i + 1
            a = a.next
        while b:
            if b in a_dict:
                return b.val
            b = b.next

    #     return None 
    def getIntersectionNode1(self, headA, headB):
        a = headA
        b = headB
        len_a = 0
        len_b = 0
        while a:
            len_a = len_a + 1
            a = a.next
        while b:
            len_b = len_b + 1
            b = b.next
        a = headA
        b = headB
        if len_a > len_b:
            temp = len_a - len_b
            while temp>0:
                a = a.next
                temp = temp - 1
        else:
            temp = len_b - len_a
            while temp>0:
                b = b.next
                temp = temp - 1 
        while a != b:
            a = a.next
            b = b.next
        if a:
            return a.val
        else:
            return None


if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    arrs1=[1,2,4]
    arrs2=[2,2,4]
    ln1 = arr2List(arrs1)
    ln2 = arr2List(arrs2)
    res=solution.getIntersectionNode(ln1, ln2)
    print(res)

    print("--------1-------")
    arrs1= [4,1,8,4,5]
    arrs2=[5,0,1,8,4,5]
    ln1 = arr2List(arrs1)
    ln2 = arr2List(arrs2)
    res=solution.getIntersectionNode(ln1, ln2)
    print(res)



    