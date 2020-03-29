'''
    在一次遍历中，怎样发现单个链表的中间元素?
'''

import sys
sys.path.append("..") # 这句是为了导入_config
from T0_ListDifine.tools import arr2List,print_list,ListNode

class Solution:
    def selectmid(self, head):
        list_len = 0
        temp_list = []
        p = head
        while p:
            list_len = list_len + 1
            temp_list.append(p)
            p = p.next
        return temp_list[int((list_len)/2)].val
        

if __name__ == "__main__":
    
    solution = Solution()

    print("----------1-----------")
    l1 = arr2List([1,2,3,4,5,6,7,8,9,10])
    print_list(l1)
    res = solution.selectmid(l1)

    print(res)
    






        


  