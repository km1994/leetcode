# 53. 最大子序和

## 题目描述

    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

## 示例:
```
   输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

## 思路介绍

### 方法一：动态规划

#### 题目解析

1. 本道题的核心需要 考虑 确定累加值 加上 当前值 后，值 和 当前值 的 大小：

#### 思路

1. 用 pre_num 保存 上一步连续子数组的最大和；
2. 遍历数组，然后做以下判断：
   1. 比较 pre_num 加上 当前值 和 当前值 的 大小，将 最大值 赋值 给 pre_num;
   2. 比较 pre_num 和 res 的大小，将 最大值 作为 当前连续子数组的最大和

    $$
        pre_num = max(pre_num,nums[i])
        res = max(pre_num,res)
    $$
   
#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(1)

### 方法二：动态规划

#### 题目解析

该问题 其实 可以转化 为 求 每一步 的 最大值：

    $$
        pre_val = max(pre_val+nums[i],nums[i])
    $$

#### 思路

对数组进行遍历，然后做以下判断：
   1. 比较 前一步最大值+当前值 与 当前值 的大小：
       
        $$pre_val = max(pre_val+nums[i],nums[i])$$

   2. 比较当前 最大值 和 最大子序列 res 的大小：
       
       $$res = max(res,pre_val)$$


#### 代码

```python
    def maxSubArray2(self, nums: List[int]) -> int:
        '''
            方法一：动态规划
                问题分析：
                    该问题 其实 可以转化 为 求 每一步 的 最大值：
                        pre_val = max(pre_val+nums[i],nums[i])

                思路：
                    对数组进行遍历，然后做以下判断：
                        1. 比较 前一步最大值+当前值 与 当前值 的大小：
                            pre_val = max(pre_val+nums[i],nums[i])
                        2. 比较当前 最大值 和 最大子序列 res 的大小：
                            res = max(res,pre_val)

        '''
        nums_len = len(nums)
        if nums_len==0:
            return 0
        pre_val = nums[0]
        res = nums[0]
        for i in range(1,nums_len):
            pre_val = nums[i] if nums[i]> pre_val+nums[i] else pre_val+nums[i]
            res = res if res>pre_val else pre_val
        return res
```

#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(1)