'''
    在未排序链表中，怎样移除重复的节点?
'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def removeRepeat(self, head):
        temp_set = set()
        p = head
        temp_set.add(p.val)
        while p.next:
            if p.next.val not in temp_set:
                temp_set.add(p.next.val)
            else:
                q = p.next
                p.next = q.next
                del q
            p = p.next


        return head

if __name__ == "__main__":
    
    solution = Solution()

    print("----------1-----------")
    l1 = arr2List([1,1,2,3,4,5,6,6,7,8,9,10])
    print_list(l1)
    res = solution.removeRepeat(l1)

    print_list(res)
    






        


  