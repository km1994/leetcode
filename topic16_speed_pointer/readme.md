# 快慢指针法

## 介绍

两个指针都从头出发，快指针移动速度比慢指针快。


## 例题介绍

### [环形链表](https://leetcode-cn.com/problems/linked-list-cycle)

#### 题目介绍

给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

```
    示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。
    示例 2：
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。
    示例 3：
    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。
```

#### 解题思路

使用快慢指针法，一个快指针，一个慢指针。如果链表不存在环，快指针会先到达链表尾部，此时就可以返回false。如果链表存在环，那么快指针最终会追上慢指针，与慢指针相遇，这时返回true。

### [快乐数](https://leetcode-cn.com/problems/happy-number)

#### 题目介绍

202. 快乐数

   编写一个算法来判断一个数 n 是不是快乐数。

    「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

    如果 n 是快乐数就返回 True ；不是，则返回 False 。

    ```
        示例：

        输入：19
        输出：true
        解释：
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1
    ```
#### 解题思路

1. 我们不是只跟踪链表中的一个值，而是跟踪两个值，称为快跑者和慢跑者。在算法的每一步中，慢速在链表中前进 1 个节点，快跑者前进 2 个节点（对 getNext(n) 函数的嵌套调用）。
2. 如果 n 是一个快乐数，即没有循环，那么快跑者最终会比慢跑者先到达数字 1。
3. 如果 n 不是一个快乐的数字，那么最终快跑者和慢跑者将在同一个数字上相遇。

## 问题介绍

### 为什么快指针一定会和慢指针相遇？

我们将慢指针的移动过程分为两个阶段：非环部分与环形部分。

1. 慢指针在走完非环部分阶段后进入环形部分：此时，快指针必然早一步进入了环形部分（因为它移动快），快指针迭代次数=非环部分长度=N。
2. 两个指针都在环形部分中：考虑两个在环形跑道上的选手，快指针叫快跑者，慢指针叫慢跑者。快跑者每次移动两步而慢跑者每次移动一步。速度差值为1，因此需要经过 （二者之间的距离/速度差值 ）次迭代后，快跑者可以与慢跑者相遇（追上）。

想象一下，在一个环形跑道上，是不可能相遇不了的，一定会相遇的。因为速度差值为1，二者之间的距离差距最大就为环形部分的长度K。每迭代一次，距离缩小1。最大的迭代次数都不会超过环形部分的长度。

### 为什么相遇就一定有环?

快指针比较快，如果没有环，它会到达NULL，结束。不会再与慢指针相遇。因此，相遇即是有环。
