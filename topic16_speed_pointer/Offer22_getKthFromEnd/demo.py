'''
    剑指 Offer 22. 链表中倒数第k个节点

    输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

    示例：

        给定一个链表: 1->2->3->4->5, 和 k = 2.

        返回链表 4->5.

'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head 
        while p and k>0:
            p = p.next 
            k = k-1
        if not p:
            return head if k == 0 else None
        q = head
        while p:
            p = p.next
            q = q.next
        return q

if __name__ == "__main__":
    solution = Solution()
    print("----------1-----------")
    l1 = arr2List([1,1,2])
    k = 2
    print_list(l1)
    res = solution.getKthFromEnd(l1,k)
    print_list(res)
    






        


  