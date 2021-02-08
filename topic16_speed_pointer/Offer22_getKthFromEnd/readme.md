# 剑指 Offer 22. 链表中倒数第k个节点

    输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

    示例：

        给定一个链表: 1->2->3->4->5, 和 k = 2.

        返回链表 4->5.

## 思路介绍

### 快慢指针

#### 题目解析

#### 思路

1. 定义 指针 p，先移动 k 个位置；
2. 定义 指针 q
3. 两个指针 同步 向 右移动，直到 p 指向 Null，此时 q 即为 答案 

#### 代码

```s
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        '''
            方法：快慢指针
            思路：
                1. 定义 指针 p，先移动 k 个位置；
                2. 定义 指针 q
                3. 两个指针 同步 向 右移动，直到 p 指向 Null，此时 q 即为 答案
        '''
        p = head 
        while p and k>0:
            p = p.next 
            k = k-1
        if not p:
            return head if k == 0 else None
        q = head
        while p:
            p = p.next
            q = q.next
        return q
```

#### 复杂度计算

> 时间复杂度： O(n)
> 
> 空间复杂度： O(1)


