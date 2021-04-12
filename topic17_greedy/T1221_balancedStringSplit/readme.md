# 1221. 分割平衡字符串

## 题目描述

在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串。

返回可以通过分割得到的平衡字符串的 最大数量 。


```s
    示例 1：
    输入：s = "RLRRLLRLRL"
    输出：4
    解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

    示例 2：
    输入：s = "RLLLLRRRLR"
    输出：3
    解释：s 可以分割为 "RL"、"LLLRRR"、"LR" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

    示例 3：
    输入：s = "LLLLRRRR"
    输出：1
    解释：s 只能保持原样 "LLLLRRRR".

    示例 4：
    输入：s = "RLRRRLLRLL"
    输出：2
    解释：s 可以分割为 "RL"、"RRRLLRLL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
     

    提示：
    1 <= s.length <= 1000
    s[i] = 'L' 或 'R'
    s 是一个 平衡 字符串
```
## 思路介绍

### 方法一：贪心算法（顺藤摸瓜）

#### 思路

1. 定义一个 结果变量 res 和一个 状态变量 num
2. 判断字符：
  2.1 if 是 R，num = num - 1
  2.2 if 是 L，num = num + 1
2. 如果 num == 0，res = res+1

#### 代码

```s
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        '''
            方法：贪心算法
            思路：
                1. 定义一个 结果变量 res 和一个 状态变量 num
                2. 判断字符：
                    2.1 if 是 R，num = num - 1
                    2.2 if 是 L，num = num + 1
                3. 如果 num == 0，res = res+1
        '''
        res = 0 
        num = 0
        for c in s:
            if c=="R":
                num=num-1
            elif c=="L":
                num=num+1
            if num == 0:
                res=res+1
        return res
```

#### 复杂度计算

> 时间复杂度：O(N)
>  
> 空间复杂度：O(N)
