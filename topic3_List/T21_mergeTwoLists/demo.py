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
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        h = head

        while l1 and l2:
            if l1.val >= l2.val:
                h.next = l2
                l2 = l2.next
            else:
                h.next = l1
                l1 = l1.next
            h = h.next
        
        if l1:
            h.next = l1
            

        if l2:
            h.next = l2 
        return head.next

if __name__ == "__main__":
    l1 = arr2List([1,2,4,5,6,8,9])
    l2 = arr2List([1,3,4])
    print_list(l1)
    print_list(l2)
    solution = Solution()
    res = solution.mergeTwoLists(l1,l2)

    print_list(res)
    






        


  