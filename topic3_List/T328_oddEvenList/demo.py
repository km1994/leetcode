'''
    328. 奇偶链表

    给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

    请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

    示例 1:

    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL
    示例 2:

    输入: 2->1->3->5->6->4->7->NULL 
    输出: 2->3->6->7->1->5->4->NULL
    说明:

    应当保持奇数节点和偶数节点的相对顺序。
    链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def oddEvenList(self, head):
        p_head = ListNode(-1)   # 奇数
        q_head = ListNode(-1)   # 偶数
        p = p_head
        q = q_head
        num = 1 
        h = head
        while h:
            if num%2 == 1:
                p.next = h
                p = p.next
            else:
                q.next = h
                q = q.next
            h = h.next
            num = num + 1
        p.next = q_head.next
        q.next = None
        return p_head.next

if __name__ == "__main__":
    
    solution = Solution()

    print("----------1-----------")
    l1 = arr2List([1,2,3,4,5,6,7,8,9])
    print_list(l1)
    res = solution.oddEvenList(l1)

    print_list(res)
    






        


  