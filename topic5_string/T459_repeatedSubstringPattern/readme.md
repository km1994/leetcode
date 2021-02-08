# 459. 重复的子字符串

## 题目描述

    给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

    示例 1:

        输入: "abab"
        输出: True

    解释: 可由子字符串 "ab" 重复两次构成。
    示例 2:

        输入: "aba"
        输出: False

    示例 3:

        输入: "abcabcabcabc"
        输出: True

    解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
     

## 思路介绍

### 方法一：枚举法

#### 思路

如果一个长度为 nn 的字符串 ss 可以由它的一个长度为 n' 的子串 s' 重复多次构成，那么：

1. n 一定是 n' 的倍数；
2. s'一定是 ss 的前缀；
3. 对于任意的 i∈[n′,n)，有 s[i] = s[i-n']。
   
#### 代码

```python
class Solution:
    # 方法一：枚举法
    def repeatedSubstringPattern1(self, s):
        '''
            思路：
                如果一个长度为 nn 的字符串 ss 可以由它的一个长度为 n' 的子串 s' 重复多次构成，那么：
                1. n 一定是 n' 的倍数；
                2. s'一定是 ss 的前缀；
                3. 对于任意的 i∈[n′,n)，有 s[i] = s[i-n']。
        '''
        s_len = len(s)
        for i in range(1,s_len//2+1):
            if s_len%i==0:
                if all(s[j]==s[j-i] for j in range(i,s_len)):
                    return True
        return False

    # 方法二：字符串匹配
    def repeatedSubstringPattern2(self, s):
        return (s+s).find(s,1)!=len(s)

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.repeatedSubstringPattern2(str1)
            print(res)
        else:
            break
```

#### 复杂度计算

> 时间复杂度：O(n^2)

> 空间复杂度：O(1)

