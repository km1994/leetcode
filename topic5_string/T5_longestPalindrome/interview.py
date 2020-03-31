'''
    5. 最长回文子串
    
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    示例 1：

    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
    示例 2：

    输入: "cbbd"
    输出: "bb"

'''
import math
class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(0,len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            s_len = len1 if len1>=len2 else len2
            if s_len > end-start:
                start = i - math.floor((s_len-1)/2)
                end = i + math.floor(s_len/2)
        return s[start:end+1]
    
    def expandAroundCenter(self,s,left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return right - left - 1

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.longestPalindrome(str1)
            print(res)
        else:
            break

