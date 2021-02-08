# 145. 二叉树的后序遍历

## 题目
### 介绍 

    给定一个二叉树，返回它的 后序 遍历。

    示例:

    输入: [1,null,2,3]  
    1
        \
        2
        /
    3 

    输出: [3,2,1]

## 解法

### 方法一 递归 or 迭代

#### 思路：


#### 代码
```s
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []             # 用于 存储 节点 的 栈
        stack.append(root)     # 先将 root 存起来
        while stack:
            curNode = stack.pop()   # 弹出 栈顶
            if curNode:
                stack.append(curNode)
                # 利用 None 作为 标识符，标识 目前 root 左右节点 以遍历，可以进行 根遍历
                stack.append(None)
                # 右左节点分别 压栈，考虑到 出栈顺序 相反
                # 先 将 右节点 压栈
                if curNode.right:
                    stack.append(curNode.right)
                # 将 左节点 压栈
                if curNode.left:
                    stack.append(curNode.left)
            else:
                # 当 遍历 到 None 时，表示 目前 栈顶元素左右子树 以遍历
                curNode = stack.pop()
                res.append(curNode.val)
        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        res = [root.val]
        return left+right+res
```

##### 复杂度计算

> 时间复杂度：O(logn)

> 空间复杂度：O(n)