#  315. 计算右侧小于当前元素的个数

## 题目描述

    给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

    示例:

        输入: [5,2,6,1]
        输出: [2,1,1,0] 
        解释:
        5 的右侧有 2 个更小的元素 (2 和 1).
        2 的右侧仅有 1 个更小的元素 (1).
        6 的右侧有 1 个更小的元素 (1).
        1 的右侧有 0 个更小的元素.

## 思路介绍

### 方法一 暴力法

#### 题目解析



#### 思路




#### 代码

```python
    import bisect
class Solution:
    def countSmaller(self, nums):
        if not nums: return []
        
        sorted_nums = []
        ans = []
        for n in nums[::-1]:
            index = bisect.bisect_left(sorted_nums,n)
            bisect.insort(sorted_nums,n)
            ans.append(index)
        return ans[::-1]

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(s) for s in str1.split(",")]
            res = solution.countSmaller(nums)
            print(res)
        else:
            break


```

#### 复杂度计算


