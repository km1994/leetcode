#  771. 宝石与石头

## 题目描述

   给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

    J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

    示例 1:

    输入: J = "aA", S = "aAAbbbb"
    输出: 3
    示例 2:

    输入: J = "z", S = "ZZ"
    输出: 0

## 思路介绍

### 方法: 哈希表法

#### 题目解析

这道题 与 两个数组的交集 I 的 区别 在于 ，这道题需要考虑重复的值，也就是 不能够直接用词典处理

#### 思路

1. 用 一个集合 diamond_set 记录 宝石类型；
2. 遍历 石头数组 J：
   1. 若是 宝石，宝石数 res + 1；

#### 代码

```s
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        if len(J)==0 or len(S)==0:
            return res 

        diamond_set = set()
        for diamond in J:
            diamond_set.add(diamond)
        
        for stone in S:
            if stone in diamond_set:
                res = res + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            nums1 = [int(num) for num in str1.split(",")]
            nums2 = [int(num) for num in str2.split(",")]
            res = solution.numJewelsInStones(nums1,nums2)
            print(res)
        else:
            break
```

#### 复杂度计算

时间复杂度：O(N+M)
空间复杂度：O(N)

