# 面试题 02.01. 移除重复节点

## 题目描述

    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

## 示例:

示例1:
    输入：[1, 2, 3, 3, 2, 1]
    输出：[1, 2, 3]
示例2:
    输入：[1, 1, 1, 1, 2]
    输出：[1, 2]
提示：
    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。

## 思路介绍

#### 题目解析


#### 思路

1. 定义采用 set 存储元素
2. 遍历 链表，判断：
   1. 定义 指针 q 指向 p.next；
   2. 如果 q.val 不在 set 中：
      1. 将 q.val  存储 到 set 中；
      2. p = p.next
   3. 否则，继续往下执行

#### 代码

```
    class Solution:
        def removeDuplicateNodes(self, head: ListNode) -> ListNode:
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
```
#### 复杂度计算

> 时间复杂度： O(n)
> 
> 空间复杂度： O(n)


