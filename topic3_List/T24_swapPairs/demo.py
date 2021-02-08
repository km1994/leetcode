'''
    24. 两两交换链表中的节点

    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

    示例 1：
    输入：head = [1,2,3,4]
    输出：[2,1,4,3]
    示例 2：

    输入：head = []
    输出：[]
    示例 3：

    输入：head = [1]
    输出：[1]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
            方法一：使用 前驱节点
        '''
        q = ListNode(0)
        q.next = head
        while q.next and q.next.next:
            q.next.val,q.next.next.val = q.next.next.val,q.next.val
            q = q.next.next
        return head
            

    def swapPairs1(self, head: ListNode) -> ListNode:
        '''
            方法二：不使用前驱节点
        '''
        if not head or not head.next:
            return head
        p = head
        q = head.next
        p.val,q.val = q.val,p.val
        while p.next.next and q.next.next:
            p = p.next.next 
            q = q.next.next
            p.val,q.val = q.val,p.val
        return head

    






        


  