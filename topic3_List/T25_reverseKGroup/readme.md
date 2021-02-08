# 25. K 个一组翻转链表

## 题目描述

    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

    k 是一个正整数，它的值小于或等于链表的长度。

    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

## 示例:
```
    示例：

    给你这个链表：1->2->3->4->5

    当 k = 2 时，应当返回: 2->1->4->3->5

    当 k = 3 时，应当返回: 3->2->1->4->5

    说明：

    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
```

## 思路介绍

### 方法一：递归法+头插法进行翻转
#### 题目解析

#### 思路

- step 1：变量定义
- step 2：计数，判断是否有 k 个节点可供翻转
- step 3：若 存在 k 个节点，则可以翻转
    - step 4：利用 头插法 翻转 k 个 节点

#### 代码

```s
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
            方法：递归法+头插法进行翻转
            思路：
                step 1：变量定义
                step 2：计数，判断是否有 k 个节点可供翻转
                step 3：若 存在 k 个节点，则可以翻转
                    step 4：利用 头插法 翻转 k 个 节点
        '''
        # step 1：变量定义
        cur = head
        check = head
        canProceed = 0
        count = 0
        prev = None
        p = None
        # step 2：计数，判断是否有 k 个节点可供翻转
        while canProceed < k and check is not None:
            check = check.next
            canProceed = canProceed + 1
        # step 3：若 存在 k 个节点，则可以翻转
        if canProceed == k:
            # step 4：利用 头插法 翻转 k 个 节点
            while count < k and cur is not None:
                p =cur.next
                cur.next = prev
                prev = cur
                cur = p
                count = count + 1
            if p is not None:
                head.next = self.reverseKGroup(p,k)
            return prev
        else:
            return head
```


#### 复杂度计算

> 时间复杂度：
> 
> 空间复杂度：


