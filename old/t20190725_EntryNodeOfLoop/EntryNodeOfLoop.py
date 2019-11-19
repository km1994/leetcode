#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: generateMatrix.py
@time: 2019/7/24
@rel： https://leetcode-cn.com/problems/spiral-matrix-ii/
@url：
@desc:
    链表中环的入口结点
        给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        pass

    def EntryNodeOfLoop(self, pHead):
        p = pHead
        if not pHead:
            return Null

        p_List = []

        while p:
            if p not in p_List:
                p_List.append(p)
                p = p.next
            else:
                return p


    '''
        工具方法 begin
    '''
    # 功能：列表转链表
    def arr2List(self, arr_list):
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

    # 功能：输出链表
    def print_list(self, ln_head):
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


if __name__ == "__main__":

    arrs=[1,4,5,1,3,4,2,6]

    solution = Solution()
    pHead = solution.arr2List(arrs)

    p = pHead
    i=0
    while i <3:
        p = p.next

     q = pHead
    while not q.next:
        q=q.next

     q.next = p

    solution.print_list(pHead)

    ln = solution.EntryNodeOfLoop(pHead)

    solution.print_list(ln)
