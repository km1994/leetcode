#  面试题 16.17. 连续数列

## 题目描述

给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

```s
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

## 思路介绍

### 方法一 动态规划法

#### 基本介绍

#### 思路

- step 1：判空
- step 2：遍历数组
  - step 3：取 pre+nums[i],nums[i] 最大值
  - step 4：记录 最大的连续数列 最大值

#### 代码

```s
class Solution(object):
    def maxSubArray(self, nums):
        """
            方法：动态规划
        """
        # step 1：判空
        nums_len = len(nums)
        if nums_len==0:
            return 0

        res = -9999999999    
        pre = 0
        # step 2：遍历数组
        for i in range(nums_len):
            # step 3：取 pre+nums[i],nums[i] 最大值
            pre = max(pre+nums[i],nums[i])
            # step 4：记录 最大的连续数列 最大值
            if pre >res:
                res = pre 
        return res
```

#### 复杂度计算

> 时间复杂度：$O(n)$

> 空间复杂度：O(1)

