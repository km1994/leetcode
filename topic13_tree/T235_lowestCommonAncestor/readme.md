# 235. 二叉搜索树的最近公共祖先

## 题目
### 介绍 

    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

    例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

    示例 1:
        输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        输出: 6 
        解释: 节点 2 和节点 8 的最近公共祖先是 6。
    示例 2:
        输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        输出: 2
        解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

## 解法

### 方法一 队列

#### 解析

- 突破点1：因为 该树 是 二叉搜索树，所以 左子树值都小于父节点值，右子树值都大于父节点值；
- 突破点2：要 寻找该树中两个指定节点的最近公共祖先，其实也就是 找到 满足 两节点 分别 位于 左右子树 的 父节点 即可； 

#### 思路

1. 递归遍历 二叉搜索树：
   1. 若 root.val > p.val and root.val > q.val，说明 最近公共祖先 位于 左子树，所以 向左子树 移动；
   2. 若 root.val < p.val and root.val > q.val，说明 最近公共祖先 位于 右子树，所以 向右子树 移动；
2. 当 p 和 q 位于 root 的 左右时，该 root 即为 最近公共祖先


#### 代码
```s
   import sys
    sys.path.append("..") # 这句是为了导入_config

    from T_tree.Tree import Tree
    import math

    class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right,p,q)
            else:
                return root
```

##### 复杂度计算

> 时间复杂度：O(logn)

> 空间复杂度：O(n)