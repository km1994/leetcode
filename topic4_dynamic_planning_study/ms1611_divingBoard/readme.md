#  面试题 16.11. 跳水板

## 题目描述

    你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

    返回的长度需要从小到大排列。

    示例：

        输入：
            shorter = 1
            longer = 2
            k = 3
        输出： {3,4,5,6}

## 思路介绍

### 方法一 动态规划法

#### 基本介绍

#### 思路

最开始全是短木板（k*shorter），然后每次都把上一次的一个短木板变为长木板。

#### 复杂度计算

> 时间复杂度：$O(n)$

> 空间复杂度：O(n)

