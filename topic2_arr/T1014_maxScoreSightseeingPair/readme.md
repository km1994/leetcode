# 1014. 最佳观光组合

## 题目描述

    给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

    一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

    返回一对观光景点能取得的最高分。

## 示例:
```
   示例：

    输入：[8,1,5,2,6]
    输出：11
    解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

```

## 思路介绍

### 方法一

#### 题目解析



#### 思路




#### 代码

```python
    class Solution:
    def maxScoreSightseeingPair(self, A):
        print(A)
        A_len = len(A)
        res = 0
        if A_len == 0:
            return res
        temp_max = A[0]
        for j in range(1,A_len):
            temp = A[j]-j
            res = res if res>temp_max+temp else temp_max+temp
            temp_max = temp_max if temp_max> A[j]+j else  A[j]+j
        return res
```

#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(1)

