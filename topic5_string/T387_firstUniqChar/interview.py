'''
    387. 字符串中的第一个唯一字符
    
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

    案例:

    s = "leetcode"
    返回 0.

    s = "loveleetcode",
    返回 2.

'''
class Solution:
    def firstUniqChar(self, s):
        for index,c in enumerate(s):
            if c not in s[0:index]+s[index+1:]:
                return index
        return -1

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.firstUniqChar(str1)
            print(res)
        else:
            break

