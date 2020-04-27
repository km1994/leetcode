# 面试题28. 对称的二叉树

## 题目
### 介绍 

    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

### 示例：

    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

    示例 1：

    输入：root = [1,2,2,3,4,4,3]
    输出：true
    示例 2：

    输入：root = [1,2,2,null,3,null,3]
    输出：false

## 解法

### 方法一 递归法

#### 思路

1. 判断 root 是否 为 None:
   1. 若是，则 返回 True;
   2. 若不是，则往下执行；
2. 判断其左右节点 是否 对称：
   1. 若 左右 节点 为 空，则 返回 True;
   2. 若 一边不为空，或值 不相等，则 返回 False;
   3. 否则，往下执行；

##### 复杂度计算

> 时间复杂度：O(n)

> 空间复杂度：O(n)