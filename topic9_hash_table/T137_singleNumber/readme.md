# 137. 只出现一次的数字 II

## 题目描述

    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

    说明：

        你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

    示例 1:
        输入: [2,2,3,2]
        输出: 3
    示例 2:
        输入: [0,1,0,1,0,1,99]
        输出: 99

## 思路介绍

1. 定义两个 集合：
  - t_set：元素出现 两次以上；
  - o_set: 元素 只 出现一次；
2. 遍历数组：
  - 如果 num 不在 t_set：
    - 如果 num 在 o_set：
          - o_set 删除 num
          - 将 num 加入 t_set
    - 否则：
        - 将 num 加入 o_set
3. 返回 list(o_set)[0]

## 代码

```python
class Solution:
    def singleNumber(self, nums):
        '''
            思路：
                1. 定义两个 集合：
                    - t_set：元素出现 两次以上；
                    - o_set: 元素 只 出现一次；
                2. 遍历数组：
                    如果 num 不在 t_set：
                        如果 num 在 o_set：
                            o_set 删除 num
                            将 num 加入 t_set
                        否则：
                            将 num 加入 o_set
                3. 返回 list(o_set)[0]
        '''
        res = 0
        if nums == []:
            return res 
        t_set = set()
        o_set = set()
        for num in nums:
            if num not in t_set:
                if num in o_set:
                    o_set.remove(num)
                    t_set.add(num)
                else:
                    o_set.add(num)
        return list(o_set)[0]

if __name__ == "__main__":   
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            res = solution.singleNumber(nums1)
            print(res)
        else:
            break
```

## 复杂度

- 时间复杂度：O(n)
- 空间复杂度：O(2n)