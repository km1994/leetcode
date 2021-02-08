#  538. 把二叉搜索树转换为累加树

## 题目
### 介绍 
 
    给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。


    例如：

    输入: 原始二叉搜索树:
              5
            /   \
           2     13
    输出: 转换为累加树:
             18
            /   \
          20     13

## 解法

### 方法一 深度遍历

#### 思路

1. 定义一个全局变量sum，用于存储遍历的所有节点值的累计和；
2. 递归终止条件： root为空就返回null;
3. 递归右子树root.right;
4. 遍历当前节点，作如下操作：
    4.1 将其值累加到sum中；
    4.2 把sum赋值给当前节点的值；
5. 递归左子树root.left;


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
    res = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        self.res =self.res+root.val
        root.val =self.res
        self.convertBST(root.left)
        return root
        
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
            res = solution.convertBST(tree.root)
            print(res)
        else:
            break
 
  
```

##### 复杂度计算

> 时间复杂度：O(n)，其中 nn 是树中的节点个数。

> 空间复杂度：O(n),空间复杂度与深度优先搜索使用的栈的最大深度相关。在最坏的情况下，树呈现链式结构，深度为 O(n)，对应的空间复杂度也为 O(n)。