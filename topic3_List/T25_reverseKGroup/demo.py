'''
    25. K 个一组翻转链表

    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

    k 是一个正整数，它的值小于或等于链表的长度。

    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    示例：

    给你这个链表：1->2->3->4->5

    当 k = 2 时，应当返回: 2->1->4->3->5

    当 k = 3 时，应当返回: 3->2->1->4->5

    说明：

    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
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

    print("----------1-----------")
    l1 = arr2List([1,2,3,4,5,6,7,8,9])
    k = 2
    print_list(l1)
    res = solution.reverseKGroup(l1,k)

    print_list(res)
    






        


  