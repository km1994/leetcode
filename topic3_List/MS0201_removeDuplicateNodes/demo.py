'''
    面试题 02.01. 移除重复节点

    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

    示例1:
        输入：[1, 2, 3, 3, 2, 1]
        输出：[1, 2, 3]
    示例2:
        输入：[1, 1, 1, 1, 2]
        输出：[1, 2]
    提示：
        链表长度在[0, 20000]范围内。
        链表元素在[0, 20000]范围内。
'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def removeDuplicateNodes(self, head):
        if not head:
            return head
        val_set = set()
        val_set.add(head.val)
        p = head
        while p.next:
            q = p.next
            if q.val not in val_set:
                val_set.add(q.val)
                p = p.next
            else:
                p.next = p.next.next
        return head
        

if __name__ == "__main__":
    
    solution = Solution()

    print("----------1-----------")
    l1 = arr2List([1, 2, 3, 3, 2, 1])
    print_list(l1)
    res = solution.removeDuplicateNodes(l1)

    print_list(res)
    






        


  