#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: removeNthFromEnd.py
@time: 2019/7/15
@rel： https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
@url：
@desc:
    19. 删除链表的倒数第N个节点
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

    示例：
        给定一个链表: 1->2->3->4->5, 和 n = 2.
        当删除了倒数第二个节点后，链表变为 1->2->3->5.





'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def removeNthFromEnd(self, head, n):
        priv_head = ListNode(0)
        priv_head.next = head

        priv_p = priv_head
        next_p = priv_head

        for i in range(0,n+1):
            priv_p = priv_p.next

        while priv_p :
            next_p = next_p.next
            priv_p = priv_p.next

        del_p = next_p.next
        next_p.next = del_p.next
        del del_p
        head = priv_head.next

        del priv_head
        return head



    def removeNthFromEnd1(self, head, n):
        priv_p = head
        p_priv_p = priv_p
        priv_next_p = head
        next_p = head

        if head.next:
            print("-2")
            head = []
            return head

        # 用 priv_p 确定第 1 个节点的 前 n 个节点
        for i in range(0,n):
            print(priv_p.val)
            if priv_p.next:
                p_priv_p.next = priv_p
                priv_p = priv_p.next
            else:
                if n == i+1:
                    print("-1")
                    p_priv_p.next = priv_p.next
                    del priv_p
                print("0")
                return head

        #print("val:{0}".format(priv_p.val))


        # 查找 链表的倒数第 n 个节点
        while priv_p:
            priv_p = priv_p.next
            priv_next_p = next_p
            next_p = next_p.next

        print("priv_next_p:{0}".format(priv_next_p.val))
        print("val:{0}".format(next_p.val))


        # 删除链表的倒数第 n 个节点
        priv_next_p.next = next_p.next
        del next_p
        return head

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

    arr1 = [1, 2, 3, 4, 5]
    n1=2

    solution = Solution()
    ln1 = solution.arr2List(arr1)

    res1 = solution.removeNthFromEnd(ln1,n1)
    solution.print_list(res1)

    arr2 = [1]
    n2 = 1

    solution = Solution()
    ln2 = solution.arr2List(arr2)

    res2 = solution.removeNthFromEnd(ln2, n2)
    solution.print_list(res2)




    

