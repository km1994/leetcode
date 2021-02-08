# 【广度优先搜索】199.二叉树的右视图

## 题目描述

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。


示例:


输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:


   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

## 思路介绍

### 方法一 层次遍历的 非递归方法

#### 基本介绍

- 找到 树 左下角的值，需要做的操作：
1. 首先需要找到 每一层最右边的值；
2. 这些值的 集合 即为 答案

#### 思路

- 方法：层次遍历的 非递归方法

- 思路：

1. 利用 层层次遍历的 非递归方法 遍历 每一层
2. 保存每一层 的 最右边一个元素；
3. 最后这些值的 集合即为 答案

#### 代码

```s
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
            方法：队列迭代 (非递归)
        '''
        res = []
        if not root:
            return res 
        queue = collections.deque()
        queue.append(root)
        while queue:
            last = -999
            for i in range(len(queue)):
                node = queue.popleft()
                last = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(last)
        return res
```
 
#### 复杂度计算

> 时间复杂度：O(N)，其中 N 是二叉树的节点数。二叉树的所有节点有且只会被访问一次，因此时间复杂度为 O(N)。
> 空间复杂度：O(N)，当树为平衡二叉树时，最多有N/2个树节点入队，使用 O(N) 大小的额外空间