'''
    242. 有效的字母异位词
    
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:

    输入: s = "rat", t = "car"
    输出: false

'''
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] = s_dict[c] + 1

        for c in t:
            if c in s_dict and s_dict[c] > 0:
                s_dict[c] = s_dict[c] - 1
            else:
                return False
        return True


if __name__ == "__main__":
    
    solution = Solution()

    while 1:
        str1 = input()
        s,t = str1.split("\t")
        if str1 != "":
            res = solution.isAnagram(s,t)
            print(res)
        else:
            break
    







        


  