# 143. 重排链表

## 题目
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


## 思路介绍

### 方法一：分而治之

#### 题目解析


#### 思路

1. 前半部分构建正序链表；
2. 后半部分构建逆序链表；
3. 合并两链表

#### 代码

```s
import sys
sys.path.append("..") # 这句是为了导入_config

from T0_ListDifine.tools import arr2List,print_list,ListNode

import math
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
            思路：
                1. 前半部分构建正序链表；
                2. 后半部分构建逆序链表；
                3. 合并两链表
        """
        if not head:
            return head
        headLen = 0
        p = head 
        while p:
            headLen = headLen+1
            p = p.next 

        mid = math.floor(headLen/2)
        reHead = ListNode()
        p = head
        q = reHead
        while mid:
            p = p.next
            mid = mid-1

        while p.next:
            tmp = q.next
            q.next = p.next
            p.next = p.next.next
            q.next.next = tmp

        self.mergeList(head,reHead.next)
        return head

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next
            l1.next = l2
            l1 = l1_tmp
            l2.next = l1
            l2 = l2_tmp

if __name__ == "__main__":
    l1 = arr2List([1,2,4,5,6,8,9])
    print_list(l1)
    solution = Solution()
    res = solution.reorderList(l1)

    print_list(res)
```

#### 复杂度计算

> 时间复杂度： O(n)
> 
> 空间复杂度： O(1)


