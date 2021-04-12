# 209. 长度最小的子数组

## 题目描述

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0



## 思路介绍

### 方法一：滑动窗口法

#### 题目解析



#### 思路



#### 代码

```s
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
            方法：滑动窗口法
        '''
        # step 1：判空
        nums_len = len(nums)
        if nums_len==0:
            return 0
        # step 2：定义左右指针
        l = 0
        r = 0
        res = nums_len+1    # res 取最大上限
        total = 0
        # step 3：滑动窗口
        while r<nums_len:
            total = total+nums[r]
            # step 4：total >= target 时，左指针需要左移，直到 total < target 
            while total>=target:
                # step 5：取最优
                res = min(res,r-l+1)       
                total = total - nums[l]
                l = l+1
            r=r+1
        return 0 if res>nums_len else res 
```

   
#### 复杂度计算

> 时间复杂度：O(n)  

> 空间复杂度：O(k)

#### 参考资料

