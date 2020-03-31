'''
    125. 验证回文串
    
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

    说明：本题中，我们将空字符串定义为有效的回文串。

    示例 1:

    输入: "A man, a plan, a canal: Panama"
    输出: true
    示例 2:

    输入: "race a car"
    输出: false


'''
class Solution:
    def isPalindrome(self, s):
        s = self.clean(s)
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        return True
        
    def clean(self,s):
        tmp = ''
        for c in s:
            if c.islower() or c.isdigit():
                tmp += c
            elif c.isupper():
                tmp += (c.lower())
        return tmp


if __name__ == "__main__":

    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.isPalindrome(str1)
            print(res)
        else:
            break


    







        


  