# 980. 不同路径 III

## 题目描述

    在二维网格 grid 上，有 4 种类型的方格：

    1 表示起始方格。且只有一个起始方格。
    2 表示结束方格，且只有一个结束方格。
    0 表示我们可以走过的空方格。
    -1 表示我们无法跨越的障碍。
    返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

## 示例:
```
  	示例 1：

    输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    输出：2
    解释：我们有以下两条路径：
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
    示例 2：

    输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    输出：4
    解释：我们有以下四条路径： 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
    示例 3：

    输入：[[0,1],[2,0]]
    输出：0
    解释：
    没有一条路能完全穿过每一个空的方格一次。
    请注意，起始和结束方格可以位于网格中的任意位置。
```

## 思路介绍

### 方法一 回溯法

#### 基本介绍

#### 思路

1. 在每到达一个结点时，首先将该点置为-1，这样是为了让之后回到该点是由于回溯，而不是在深搜过程中回到该点，陷入死循环。 
2. 每次将当前的点置为-1后，图中的0的个数也减少了一个，这个可以用一个变量来记录，作为走到2时是否走完所有0的判断依据。
3. 在这个结点进行递归搜索，搜索结束回到这个点时，应该将其还原为0，这是因为在回溯算法中，必须要在递归结束后，回溯到上一个结点前，将当前状 态恢复成递归前的状态，这一点对理解回溯思想非常重要。
   
#### 复杂度计算

> 时间复杂度：O(4^(R*C))

> 空间复杂度：O(R*C)

