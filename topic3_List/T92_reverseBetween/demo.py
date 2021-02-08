'''
    21. 合并两个有序链表
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
'''

import sys
sys.path.append("..") # 这句是为了导入_config

from T0_ListDifine.tools import arr2List,print_list,ListNode


class Solution:
    def reverseBetween(self, head, m, n):
        prehead = ListNode(-1)
        prehead.next = head
        pre = prehead
         # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
        for _ in range(m - 1):
            pre = pre.next
        # 用 pre, start, tail三指针实现插入操作
        # tail 是插入pre,与pre.next的节点
        start = pre.next
        tail = start.next
        for _ in range(n - m):
            start.next = tail.next
            tail.next = pre.next
            pre.next = tail
            tail = start.next
        return prehead.next
        

if __name__ == "__main__":
    l1 = arr2List([1,2,4,5,6,8,9])
    m = 2, n = 4
    print_list(l1)
    solution = Solution()
    res = solution.reverseBetween(l1,m,n)

    print_list(res)
    






        


  