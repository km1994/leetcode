#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: divide.py
@time: 2019/4/17 11:56
@desc:
    23. 合并K个排序链表
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    示例:
        输入:
            [
              1->4->5,
              1->3->4,
              2->6
            ]
        输出: 1->1->2->3->4->4->5->6
'''

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        pass

    def mergeKLists(self, lists ):
        if len(lists) == 0:
            return []
        if len(lists)==1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0],lists[1])

        kList = lists[0]
        for i in range(1,len(lists)):
            #print("i:{0}".format(i))
            kList = self.mergeTwoLists(kList,lists[i])
        return kList

    def mergeTwoLists(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1

        ln_head = ListNode('')
        p = ln_head
        while list1 and list2:
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            p=p.next

        if list1:
            p.next = list1

        if list2:
            p.next = list2

        ln_head=ln_head.next
        return ln_head


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

    arrs=[
        [1,4,5],
        [1,3,4],
        [2,6]
    ]
    lists=[]

    solution = Solution()

    for arr in arrs:
        ln = solution.arr2List(arr)
        lists.append(ln)

    kList=solution.mergeKLists(lists)
    solution.print_list(kList)
