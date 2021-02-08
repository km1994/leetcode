#  面试题 17.16. 按摩师

## 题目描述

    一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

    注意：本题相对原题稍作改动

    示例 1：

    输入： [1,2,3,1]
    输出： 4
    解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
    示例 2：

    输入： [2,7,9,3,1]
    输出： 12
    解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
    示例 3：

    输入： [2,1,4,5,3,1,1,3]
    输出： 12
    解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

## 思路介绍

### 方法一 动态规划法

#### 解析：
    每个位置 有 can or cannot 两种可能
#### 状态方程：
- cannot = max(cannot,can)  # 如果这个位置不取，最大值为 上个位置 cannot 或 can 的最大值；
- can = max(can,cannot+num) # 如果这个位置取，最大值为 上个位置 can 或 上个位置cannot+num 间最大值
#### 代码

```s
class Solution:
    # 动态规划法
    def massage(self, nums):
        can = 0
        cannot = 0
        for num in nums:
            cannot,can = max(cannot,can),max(can,cannot+num)
        return max(can,cannot)

    def massage2(self, nums):
        '''
            方法一：动态规划（常数空间）
            解析：
                每个位置 有 can or cannot 两种可能
            状态方程：
                cannot = max(cannot,can)  # 如果这个位置不取，最大值为 上个位置 cannot 或 can 的最大值；
                can = max(can,cannot+num) # 如果这个位置取，最大值为 上个位置 can 或 上个位置cannot+num 间最大值
        '''
        can = 0
        cannot = 0
        for num in nums:
            cannot,can = cannot if cannot>can else can, can if can>cannot+num else cannot+num
        return cannot if cannot>can else can

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            nums = [int(num) for num in str1.split(",")]
            res = solution.massage(nums)
            print(res)
        else:
            break
```

#### 复杂度计算

> 时间复杂度：$O(n)$

> 空间复杂度：O(1)

