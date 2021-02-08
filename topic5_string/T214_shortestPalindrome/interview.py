'''
    214. 最短回文串
    
    给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

    示例 1:

    输入: "aacecaaa"
    输出: "aaacecaaa"
    示例 2:

    输入: "abcd"
    输出: "dcbabcd"

'''
class Solution:
    # 方法一：对称
    def shortestPalindrome(self, s):
        '''
            思路：找到 反向的第一个重合点
        '''
        r = s[::-1]
        print(f"s:{s}")
        print(f"r:{r}")
        for i in range(len(s)+1):
            print(f"r[{i}:]:{r[i:]}")
            if s.startswith(r[i:]):
                return r[:i]+s

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.shortestPalindrome(str1)
            print(res)
        else:
            break

