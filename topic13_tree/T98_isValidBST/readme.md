#  98. 验证二叉搜索树

## 题目
### 介绍 

       
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

### 示例：

    示例 1:

    输入:
    2
   / \
  1   3
    输出: true
    示例 2:

    输入:
    5
   / \
  1   4
     / \
    3   6
    输出: false
    解释: 输入为: [5,1,4,null,null,3,6]。
         根节点的值为 5 ，但是其右子节点值为 4 。
## 解法

### 方法一 中序遍历

#### 思路

1.  观察到中序遍历的顺序是左->中->右,也就是按照从小到大的顺序，因此这样思考题目就很好解了,按照中序遍历，将值依次存入列表中。最后判断


##### 复杂度计算

> 时间复杂度：

> 空间复杂度：