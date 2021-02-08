'''
    1002. 查找常用字符
    
    给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

    你可以按任意顺序返回答案。

    示例 1：

    输入：["bella","label","roller"]
    输出：["e","l","l"]
    示例 2：

    输入：["cool","lock","cook"]
    输出：["c","o"]

'''
from collections import defaultdict
class Solution:
    # 方法一：哈希表法
    def commonChars(self, A):
        '''
            思路：
                
        '''
        minfreq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])
        
        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans
        # minfreq = defaultdict(int)
        # for word in A:
        #     freq = defaultdict(int)
        #     for ch in word:
        #         freq[ord(ch)-ord("a")]+=1
        #     print(f"freq:{freq}")
        #     for (key,val) in freq.items():
        #         print(f"key:{key},val:{val}")
        #         if key not in minfreq:
        #             minfreq[key] = 0
        #         minfreq[key] = min(minfreq[key],val)
        # print(f"minfreq:{minfreq}")  
        # res = []
        # for (key,val) in minfreq.items():
        #     res.extend([chr(key + ord("a"))]*val)
        # return res

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            A = str1.split(",")
            res = solution.commonChars(A)
            print(res)
        else:
            break

