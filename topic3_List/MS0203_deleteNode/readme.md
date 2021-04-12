# 面试题 02.03. 删除中间节点

## 题目描述

    实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。

## 示例:
```
    示例：

    输入：单向链表a->b->c->d->e->f中的节点c
    结果：不返回任何数据，但该链表变为a->b->d->e->f
```

## 思路介绍

### 方法一 

#### 题目解析

1. 因为 node 的节点值 是要删除的节点值

#### 思路

1. step 1 将 node.next 值 覆盖 node 值
2. step 2：记录当前节点，方便后期删除
3. step 3：指针移动

#### 代码

```s
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
            解析：因为 node 的节点值 是要删除的节点值
            思路：
                step 1 将 node.next 值 覆盖 node 值
                step 2：记录当前节点，方便后期删除
                step 3：指针移动
            复杂度：
                时间：O(1)
                空间：O(1)
        """
        # step 1 将 node.next 值 覆盖 node 值
        node.val = node.next.val 
        # step 2：记录当前节点，方便后期删除
        tmp_node = node.next
        # step 3：指针移动
        node.next = node.next.next  
        del tmp_node         # 删除节点，防止泄露
```

#### 复杂度计算

> 时间复杂度： O(1)
> 
> 空间复杂度： O(1)

