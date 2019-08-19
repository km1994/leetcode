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
    148. 排序链表
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

    示例 1:
        输入: 4->2->1->3
        输出: 1->2->3->4
    示例 2:
        输入: -1->5->3->4->0
        输出: -1->0->3->4->5
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

    def sortList(self, head):
        self.print_list(head)
        if not head:
            return None
        pre_head = ListNode(0)
        sort_head = ListNode(0)
        s = sort_head
        pre_head.next = head
        q = pre_head
        while q.next:
            min_p = q
            if min_p.next:
                p = min_p.next
                while p.next:
                    print("min_p.next.val:{0}".format(min_p.next.val))
                    print("p.next.val:{0}".format(p.next.val))
                    if p.next.val < min_p.next.val:
                        min_p = p
                    p = p.next
                print("min_p.next.val:{0}".format(min_p.next.val))
                s.next = min_p.next
                s = s.next
                min_p.next = s.next
            else:
                s.next = min_p
                q.next = None
        
        sort_head = sort_head.next
        self.print_list(sort_head)

        return sort_head

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
        else:
            return None

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

    print("--------1-------")
    arrs=[4,2,1,3]
    solution = Solution()
    ln = solution.arr2List(arrs)
    res=solution.sortList(ln)
    solution.print_list(res)

    print("--------2-------")
    arrs=[]
    solution = Solution()
    ln = solution.arr2List(arrs)
    res=solution.sortList(ln)
    solution.print_list(res)

    print("--------3-------")
    arrs=[3]
    solution = Solution()
    ln = solution.arr2List(arrs)
    res=solution.sortList(ln)
    solution.print_list(res)


    print("--------4-------")
    arrs=[-1,5,3,4,0]
    solution = Solution()
    ln = solution.arr2List(arrs)
    res=solution.sortList(ln)
    solution.print_list(res)


