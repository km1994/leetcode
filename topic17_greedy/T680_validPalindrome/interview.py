'''
    680. 验证回文字符串 Ⅱ

    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

    示例 1:

    输入: "aba"
    输出: True
    示例 2:

    输入: "abca"
    输出: True
    解释: 你可以删除c字符。
    注意:

    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

'''
class Solution:
    # 贪心算法
    def validPalindrome(self, s):
        # 验证字符串是否是回文
        def isPalindrome(left,right):
            i = left
            j = right
            while i<j:
                if s[i]!=s[j]:
                    return False
                i = i + 1
                j = j - 1
            return True
        
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]==s[right]:
                left = left +1
                right= right-1
            else:
                return isPalindrome(left+1,right) or isPalindrome(left,right-1)
            return True

   
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            
            res = solution.validPalindrome(str1)
            print(res)
        else:
            break

