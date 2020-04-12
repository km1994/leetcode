'''
    22. 括号生成
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

    示例：

    输入：n = 3
    输出：[
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
        ]

'''
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def generateParenthesis(self, n):
        res = []
        def backtrack(S,l,r):
            if len(S) == 2*n:
                res.append("".join(S))
                return
            if l < n:
                S.append('(')
                backtrack(S,l+1,r)
                S.pop()
            if r<l:
                S.append(")")
                backtrack(S,l,r+1)
                S.pop()

        backtrack([],0,0)
        return res
    
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = int(str1)
            res = solution.generateParenthesis(nums1)
            print(res)
        else:
            break

