'''
    139. 单词拆分

    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

    说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
    示例 1：

    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
    示例 2：

    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
         注意你可以重复使用字典中的单词。
    示例 3：

    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false

'''
class Solution:
    # 动态规划
    def wordBreak(self, s, wordDict):
        s_len = len(s)
        s_flag_list = [False for _ in range(s_len+1)]
        s_flag_list[0] = True
        for i in range(s_len):
            for j in range(i+1,s_len+1):
                if s_flag_list[i] and s[i:j] in wordDict:
                    s_flag_list[j] = True
        return s_flag_list[-1]

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            wordDict = [word for word in str1.split(",")]
            s = str2
            res = solution.wordBreak(s,wordDict)
            print(res)
        else:
            break

