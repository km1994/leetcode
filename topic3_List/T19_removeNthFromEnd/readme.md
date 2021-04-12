# 19. 删除链表的倒数第 N 个结点

## 题目描述

    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

    进阶：你能尝试使用一趟扫描实现吗？

```s  
    示例 1：
        输入：head = [1,2,3,4,5], n = 2
        输出：[1,2,3,5]
    示例 2：
        输入：head = [1], n = 1
        输出：[]
    示例 3：
        输入：head = [1,2], n = 1
        输出：[1]
```

## 思路介绍

### 方法

#### 题目解析



#### 思路

1. step 1：定义前驱节点
2. step 2：找到 要删除的节点的前驱
3. step 3：删除节点

#### 代码

```s
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # step 1：定义前驱节点
        priv_head = ListNode(0)
        priv_head.next = head
        # step 2：找到 要删除的节点的前驱
        p = priv_head
        q = priv_head 
        while p:
            if n>=0:
                n=n-1
            else:
                q = q.next 
            p = p.next
        # step 3：删除节点
        tmp = q.next 
        q.next = q.next.next 
        del tmp
        return priv_head.next
```

#### 复杂度计算

> 时间复杂度： O(N)
> 
> 空间复杂度： O(1)

