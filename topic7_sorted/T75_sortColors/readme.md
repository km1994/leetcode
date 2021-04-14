# 75. 颜色分类

## 题目描述


给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。


示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]


## 思路介绍

### 方法

#### 思路

 

#### 代码

```s
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        题目：75.颜色分类
        """
        left,cur = 0,0
        right = len(nums)-1
        while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left] = nums[left],nums[cur]
                cur = cur+1
                left = left+1
            elif nums[cur]==2:
                nums[cur],nums[right] = nums[right],nums[cur]
                right = right-1
            else:
                cur = cur+1
``` 
#### 复杂度计算

- 时间复杂度：O(NlogN)
- 空间复杂度：O(N)

