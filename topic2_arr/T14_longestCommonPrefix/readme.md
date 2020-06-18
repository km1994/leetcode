# 14. 最长公共前缀

## 题目描述

    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

## 示例:
```
   示例 1:

    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:

    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

```

## 思路介绍

### 方法一

#### 题目解析



#### 思路

多路归并


#### 代码

```python
    class Solution:
    def longestCommonPrefix(self, strs):
        strs_len = len(strs)
        if not strs_len:
            return ""
        common_str = strs[0]
        for i in range(1,strs_len):
            common_str = self.common(common_str,strs[i])
        return common_str
        

    def common(self,s1,s2):
        common_str = []
        s1_len = len(s1)
        s2_len = len(s2)
        min_len = s1_len if s1_len<s2_len else s2_len
        for i in range(min_len):
            if s1[i]==s2[i]:
                common_str.append(s1[i])
            else:
                return ''.join(common_str)
        return ''.join(common_str)   


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            strs = str1.split(",")
            res = solution.longestCommonPrefix(strs)
            print(res)
        else:
            break
```

#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(1)

