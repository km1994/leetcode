# 572. 另一个树的子树

## 题目
### 介绍 

    给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

### 示例：

        示例 1:
    给定的树 s:

     3
    / \
   4   5
  / \
 1   2
    给定的树 t：

   4 
  / \
 1   2
    返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

    示例 2:
    给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
    给定的树 t：

   4
  / \
 1   2
    返回 false。

## 解法

### 方法一 回溯法

#### 思路

1. 遍历两棵树的每个节点；
2. 检查 对应节点是否相等（左右孩子有无一致 and 根节点值 相同）；
   1. 若一致，同时向左右孩子 遍历 并 比较；
   2. 不一致，s 往 左右 节点 移动

##### 复杂度计算

> 时间复杂度：$O(|s|*|t|)$

> 空间复杂度：$O(max(d_s,d_t))$