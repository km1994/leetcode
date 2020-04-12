'''
    131. 分割回文串
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

    返回 s 所有可能的分割方案。

    示例:

    输入: "aab"
    输出:
    [
    ["aa","b"],
    ["a","a","b"]
    ]

'''
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def partition(self, s):
        s_len = len(s)
        res = []
        if s_len == 0:
            return res
        def backtrack(s,start,s_len,path):
            if start == s_len:
                res.append(path[:])
                return
            for i in range(start,s_len):
                # 如果 s[start:i] 不是回文，直接剪枝
                if not self.checkPalindrome(s,start,i):
                    continue

                path.append(s[start:i+1])
                backtrack(s,i+1,s_len,path)
                path.pop()

        backtrack(s,0,s_len,[])
        return res

    def checkPalindrome(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.partition(str1)
            print(res)
        else:
            break

