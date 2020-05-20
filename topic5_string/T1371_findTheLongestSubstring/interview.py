'''
    1371. 每个元音包含偶数次的最长子字符串
    
    给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

    示例 1：

    输入：s = "eleetminicoworoep"
    输出：13
    解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
    示例 2：

    输入：s = "leetcodeisgreat"
    输出：5
    解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
    示例 3：

    输入：s = "bcbcbc"
    输出：6
    解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
     

    提示：

    1 <= s.length <= 5 x 10^5
    s 只包含小写英文字母。

'''
class Solution:
    def __init__(self):
        self.i_mapper = {
            "a": 0,
            "e": 1,
            "i": 2,
            "o": 3,
            "u": 4
        }
        
    def check(self, s, pre, l, r):
        for i in range(5):
            if s[l] in self.i_mapper and i == self.i_mapper[s[l]]: cnt = 1
            else: cnt = 0
            if (pre[r][i] - pre[l][i] + cnt) % 2 != 0: return False
        return True
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)

        pre = [[0] * 5 for _ in range(n)]

        # pre
        for i in range(n):
            for j in range(5):
                if s[i] in self.i_mapper and self.i_mapper[s[i]] == j:
                    pre[i][j] = pre[i - 1][j] + 1
                else:
                    pre[i][j] = pre[i - 1][j]
        for i in range(n - 1, -1, -1):
            for j in range(n - i):
                if self.check(s, pre, j, i + j):
                    return i + 1
        return 0

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.findTheLongestSubstring(str1)
            print(res)
        else:
            break

