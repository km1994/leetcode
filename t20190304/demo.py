'''
	给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

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
        
        if len(s) < 1:
            return ''

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self. expandAroundCenter(s,i,i+1)
            len_max = max(len1,len2)
            
            if len_max > end-start:
                start = i -int((len_max-1)/2)
                end = i + int(len_max/2)
            
        print(f"start:{start},end:{end}")
        return s[start:end+1]
        
    def expandAroundCenter(self,  s : str, left : int, right : int) -> int:
        L = left
        R = right
        while L>=0 and R<len(s) and s[L] == s[R]:
            L = L - 1
            R = R + 1 
        
        return R - L -1

if __name__ == "__main__":
    solution = Solution()
    str1=solution.longestPalindrome("ABABADE")
    print(f"str1:{str1}")