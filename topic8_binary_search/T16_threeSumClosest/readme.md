# 16. 最接近的三数之和

## 题目描述

    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

## 示例:

```
    示例：

    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
```

## 思路介绍

### 方法一: 排序 + 双指针

#### 题目解析

#### 思路


#### 代码

```python
    class Solution:
        def threeSumClosest(self, nums: List[int], target: int) -> int:
            nums.sort()
            closeSum = nums[0] + nums[1] +nums[2]
            for i in range(len(nums)-2):
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if math.fabs(target - s) < math.fabs(target - closeSum):
                        closeSum = s
                    elif s > target:
                        r -=1
                    elif s < target:
                        l +=1
                    else:
                        return closeSum
            return closeSum
```

 
#### 复杂度计算

时间复杂度：O(NlogN)
空间复杂度：O(N)

