# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # step 1：定义前驱节点
        priv_head = ListNode(0)
        priv_head.next = head
        # step 2：找到 要删除的节点的前驱
        p = priv_head
        q = priv_head 
        while p:
            if n>=0:
                n=n-1
            else:
                q = q.next 
            p = p.next
        # step 3：删除节点
        tmp = q.next 
        q.next = q.next.next 
        del tmp
        return priv_head.next