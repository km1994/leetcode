#  198. 打家劫舍

## 题目描述

    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

## 示例:
```
  	示例 1:

    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

## 思路介绍

### 方法一 动态规划法 列表存储

#### 基本介绍

这道题可以转化为计算每个位置的最大值，可以采用动态规划方法处理

#### 思路

1. 定义一个 res 保存当前最大值，默认值为 num[0]；
2. 遍历数组 1-> nums_len:
   1. 若 i == 1: (也就是第二个位置)
      1. 第二个位置的值的最优为上一个位置或当前位置的最优，所以可以采用以下公式计算：
   
        $nums[i] = nums[i] if nums[i]>nums[i-1] else nums[i-1]$

   2. 若 为 [2,nums_len]:
      1. 第二个位置的值的最优为 上上个位置的最优加当前位置的值 或 上个位置的值的最优 的相对大值

        $$
            temp = nums[i]+nums[i-2]
            nums[i] = temp if temp>nums[i-1] else nums[i-1]
        $$
    1. 当前位置的最大值 为 当前位置值 与 上一个位置的最优 的相对最大值
        $$
            res = nums[i] if nums[i]>res else res
        $$

#### 代码

```python
    def rob(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        res = nums[0]
        for i in range(1,nums_len):
            if i == 1:
                nums[i] = nums[i] if nums[i]>nums[i-1] else nums[i-1]
            else:
                temp = nums[i]+nums[i-2]
                nums[i] = temp if temp>nums[i-1] else nums[i-1]
            res = nums[i] if nums[i]>res else res
        return res
```

#### 复杂度计算

> 时间复杂度：$O(n)$

> 空间复杂度：O(n)

### 方法二 动态规划法 上一个值存储

#### 基本介绍

重新考虑该问题，你会发现，其实当前值仅与 上一个值相关，那么我们是否可以只保留 上一个值 呢？

答案是可以的

#### 思路

```python
    def rob(self, nums):
        pre = 0
        res = 0
        for num in nums:
            temp = pre+num
            pre = temp if temp>res else res
            pre,res = res,pre
        return res
```

#### 复杂度计算

> 时间复杂度：$O(n)$

> 空间复杂度：O(1)