# 面试题 16.18. 模式匹配

## 题目描述

   你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
     
## 示例:
```
    示例 1：
        输入： pattern = "abba", value = "dogcatcatdog"
        输出： true
    示例 2：
        输入： pattern = "abba", value = "dogcatcatfish"
        输出： false
    示例 3：
        输入： pattern = "aaaa", value = "dogcatcatdog"
        输出： false
    示例 4：
        输入： pattern = "abba", value = "dogdogdogdog"
        输出： true
    解释： "a"="dogdog",b=""，反之也符合规则
```

## 思路介绍

### 方法一

#### 题目解析

#### 思路

```python
    class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        cnta, cntb, n = 0, 0, len(value)         # 计算a和b的个数，n为value长度
        for ch in pattern:
            if ch == 'a': cnta += 1
            else: cntb += 1
        
        if n == 0:                               # 判断各种边界情况，pattern或者value为空
            return cnta * cntb == 0
        else:
            if cnta == 0 and cntb == 0:
                return False
            elif cnta == 0 or cntb == 0:         # 判断pattern全是a或者全是b的情况
                if cnta == 0:
                    cnta, cntb = cntb, cnta      # 如果cnta为0，两者调换一下
                if n % cnta != 0:                # 不能整除的情况
                    return False
                d, judge = n//cnta, set()        # 用集合来判断是否有第二种字符串出现
                for i in range(cnta):
                    judge.add(value[i*d:i*d+d-1])
                    if len(judge) > 1: break
                return len(judge) == 1           # 如果自始至终只有一种字符串，那么就是True

        for i in range(0, n//cnta+1):            # 一般情况
            if (n-i*cnta) % cntb == 0:           # 只判断能整除的情况
                j = (n-i*cnta)//cntb
                cur, judge1, judge2 = 0, set(), set()
                for ch in pattern:               # 分别判断两个集合是否有第二种字符串出现
                    if ch == 'a':
                        judge1.add(value[cur:cur + i])
                        cur += i
                    else:
                        judge2.add(value[cur:cur + j])
                        cur += j
                    if len(judge1) > 1 and len(judge2) > 1:
                        break
                if len(judge1) == 1 and len(judge2) == 1:
                    return True                   # 如果两个集合都只有一种字符串，那么就是True
        return False
```
 
#### 复杂度计算

> 时间复杂度：
> 
> 空间复杂度：

