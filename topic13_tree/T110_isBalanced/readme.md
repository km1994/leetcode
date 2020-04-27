# 110. 平衡二叉树

## 题目介绍

### 介绍 

    给定一个二叉树，判断它是否是高度平衡的二叉树。

    本题中，一棵高度平衡二叉树定义为：

    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

### 示例：

    示例 1:

    给定二叉树 [3,9,20,null,null,15,7]

     3
    / \
   9  20
     /  \
    15   7
    返回 true 。

    示例 2:

    给定二叉树 [1,2,2,3,3,null,null,4,4]

         1
        / \
       2   2
     / \
    3    3
    / \
   4   4
    返回 false 。

## 解法

### 方法一 暴力法

#### 题目解析

1. 对于该问题，若当前子树平衡，那么她需要同时满足以下条件：
   1. 当前子树平衡：abs(height(root.left) - height(root.right)) <2;
   2. 左子树 平衡： isBalanced(root.left)；
   3. 右子树 平衡： isBalanced(root.right)；

#### 思路

1. 若树为空，那么 该树 平衡；
2. 若树不为空：
   1. 需要满足以下条件：
      1. abs(height(root.left) - height(root.right)) <2
      2. isBalanced(root.left)
      3. isBalanced(root.right)

##### 复杂度计算

> 时间复杂度：O(logn)

> 空间复杂度：O(n)