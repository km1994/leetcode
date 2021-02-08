'''
    392. 判断子序列
    
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

    你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

    字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

    示例 1:
    s = "abc", t = "ahbgdc"

    返回 true.

    示例 2:
    s = "axc", t = "ahbgdc"

    返回 false.

'''
class Solution:
    def isAnagram(self, s, t):
        s_len = len(s)
        t_len = len(t)
        p = 0
        q = 0
        while p<s_len and q<t_len:
            if s[p]==t[q]:
                p = p+1
                q = q+1
            else:
                q=q+1
        if p==s_len:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "":
            s = str1
            t = str2
            res = solution.isAnagram(s,t)
            print(res)
        else:
            break
    







        


  