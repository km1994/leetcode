'''
    23. 合并K个排序链表

    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

    示例:

    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6

'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def mergeKLists(self, lists):
        lists_len = len(lists)
        if lists_len == 0:
            return 
        return self.merge(lists,0,lists_len-1)

    def merge(self,lists,left,right):
        if left == right:
            return lists[left]
        mid = left+(right-left)//2
        l1 = self.merge(lists,left,mid)
        l2 = self.merge(lists,mid+1,right)
        return self.mergeTwoList(l1,l2)
    
    def mergeTwoList(self,l1,l2):
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
    
    solution = Solution()

    print("----------1-----------")
    lists = []
    l1 = arr2List([1,3,5,6])
    l2 = arr2List([2,4,9])
    l3 = arr2List([7,8])
    print_list(l1)
    print_list(l2)
    print_list(l3)
    lists.append(l1)
    lists.append(l2)
    lists.append(l3)
    res = solution.mergeKLists(lists)

    print_list(res)
    






        


  