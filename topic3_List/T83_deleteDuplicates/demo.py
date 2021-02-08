'''
    83. 删除排序链表中的重复元素

    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

    示例 1:

        输入: 1->1->2
        输出: 1->2
        示例 2:

        输入: 1->1->2->3->3
        输出: 1->2->3

'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def deleteDuplicates(self, head):
        '''
            思路：
                1. 判断 head 是否为空？
                2. p 指向 head
                3. 遍历 p:
                    若 p.val 与 p.next.val 相等时，删除 p.next；
                    否则，继续遍历
        '''
        if not head:
            return head
        p = head
        while p.next:
            if p.val==p.next.val:
                q = p.next
                p.next = q.next
                q = None
            else:
                p = p.next
        return head
        

if __name__ == "__main__":
    
    solution = Solution()

    print("----------1-----------")
    l1 = arr2List([1,1,2])
    print_list(l1)
    res = solution.deleteDuplicates(l1)

    print_list(res)
    






        


  