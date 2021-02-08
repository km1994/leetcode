# 404. 左叶子之和

## 题目
### 介绍 
 
    计算给定二叉树的所有左叶子之和。

    示例：

    3
   / \
  9  20
    /  \
   15   7

    在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

## 解法

### 方法一 深度遍历

#### 思路

1.  一个节点为「左叶子」节点，当且仅当它是某个节点的左子节点，并且它是一个叶子结点。因此我们可以考虑对整棵树进行遍历，当我们遍历到节点 \textit{node}node 时，如果它的左子节点是一个叶子结点，那么就将它的左子节点的值累加计入答案。

#### 代码

```python
import sys
sys.path.append("..") # 这句是为了导入_config
from T_tree.Tree import Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self,root):
        res = 0
        if root.left:
            if self.isLeafNode(root.left):
                res = res + root.left.val
            else:
                res = res+self.dfs(root.left)
        if root.right and not self.isLeafNode(root.right):
            res = res+self.dfs(root.right)
        return res

    def isLeafNode(self,node):
        return not node.left and not node.right
        
if __name__ == "__main__":
    tree = Tree()
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            node_list = str1.split(",")
            for node in node_list:
                tree.add(node)
            print(f"层次遍历：{tree.traverse(tree.root)}")
            res = solution.sumOfLeftLeaves(tree.root)
            print(res)
        else:
            break
```

##### 复杂度计算

> 时间复杂度：O(n)，其中 nn 是树中的节点个数。

> 空间复杂度：O(n),空间复杂度与深度优先搜索使用的栈的最大深度相关。在最坏的情况下，树呈现链式结构，深度为 O(n)，对应的空间复杂度也为 O(n)。