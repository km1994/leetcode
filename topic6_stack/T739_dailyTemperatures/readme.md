# 739. 每日温度

## 题目描述

    请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

    提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

## 思路介绍

### 方法一 暴力法

#### 题目解析



#### 思路




#### 代码

```python
    class Solution:
        def dailyTemperatures1(self, T):
        res = []
        T_len = len(T)
        for i in range(T_len):
            for j in range(i+1,T_len):
                if T[i]<T[j]:
                    res.append(j-i)
                    break
                if j==T_len-1:
                    res.append(0)
        res.append(0)
        return res
```

#### 复杂度计算

> 时间复杂度：O(n^2)
>  
> 空间复杂度：O(n)

### 方法二 栈

#### 题目解析



#### 思路

```python
    def dailyTemperatures(self, T):
        T_len = len(T)
        res = [0] * T_len
        stack = []
        for i in range(T_len):
            temp = T[i]
            while stack and temp >T[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i-prev_index
            stack.append(i)
        return res
```
#### 复杂度计算

> 时间复杂度：O(n^2)
>  
> 空间复杂度：O(n)