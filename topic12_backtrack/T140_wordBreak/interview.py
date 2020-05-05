'''
    140. 单词拆分 II

    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

    说明：

    分隔时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
    示例 1：

    输入:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    输出:
    [
      "cats and dog",
      "cat sand dog"
    ]
    示例 2：

    输入:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    输出:
    [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    解释: 注意你可以重复使用字典中的单词。
    示例 3：

    输入:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出:
    []

'''
class Solution:
    # 回溯法
    def wordBreak(self, s, wordDict):
        s_len = len(s)
        res = []
        memo = {s_len: ['']}  # 初始化记忆化存储
        if not s_len:
            return res
        wordDict = set(wordDict) # 转换成字典用于O(1)判断in
        # 记录字典中的单词的最长和最短长度，用于剪枝
        word_min = 9999 
        word_max = -9999
        for word in wordDict:
            word_min = word_min if word_min<len(word) else len(word)
            word_max = word_max if word_max>len(word) else len(word)
        def backtrack(start):   # 返回s[start:]能由字典构成的所有句子
            if start not in memo:
                res = []
                # 剪枝，只考虑从最小长度到最大长度查找字典
                for i in range(word_min,min(word_max,s_len-start)+1): 
                    # 找到了
                    if s[start:start+i] in wordDict:
                        # 添加到结果中
                        res.extend(list(map(lambda x: s[start: start+i]+' '+x, backtrack(start+i))))  # 添加
                memo[start] = res  # 加入记忆
            return memo[start]
        
        return list(map(lambda x: x[:-1], backtrack(0)))  # 去掉末尾多出的一个空格




        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            wordDict = [word for word in str1.split(",")]
            s = str2
            res = solution.wordBreak(s,wordDict)
            print(f"res:{res}")
        else:
            break

