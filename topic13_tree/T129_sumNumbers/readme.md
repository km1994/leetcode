# 129. 求根到叶子节点数字之和

## 题目
### 介绍 

    
    给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

    例如，从根到叶子节点路径 1->2->3 代表数字 123。

    计算从根到叶子节点生成的所有数字之和。

    说明: 叶子节点是指没有子节点的节点。

### 示例：

    示例 1:

    输入: [1,2,3]
    1
   / \
  2   3
    输出: 25
    解释:
    从根到叶子节点路径 1->2 代表数字 12.
    从根到叶子节点路径 1->3 代表数字 13.
    因此，数字总和 = 12 + 13 = 25.
    示例 2:

    输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
    输出: 1026
    解释:
    从根到叶子节点路径 4->9->5 代表数字 495.
    从根到叶子节点路径 4->9->1 代表数字 491.
    从根到叶子节点路径 4->0 代表数字 40.
    因此，数字总和 = 495 + 491 + 40 = 1026.

## 解法

### 方法一 回溯法

#### 思路

1. 定义 res 用于 存储结果；
2. 定义一个 temp_sum 用于存储临时 值；
3. 将当前节点值 加入 temp_sum ： temp_sum = temp_sum*10 + root.val;
4. 判断 当前节点是否 叶子 节点：
   1. 是，将 temp_sum 加入 res:  self.res = self.res + temp_sum
   2. 回退：temp_sum = int((temp_sum-root.val)/10) 
5. 判断 左子树 是否存在：
   1. 是，左子树遍历；
6. 判断右子树 是否存在：
   1. 是，右子树遍历；

##### 复杂度计算

> 时间复杂度：O(logn)

> 空间复杂度：O(n)