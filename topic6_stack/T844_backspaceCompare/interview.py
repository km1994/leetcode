'''
    844. 比较含退格的字符串
    
    给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

    注意：如果对空文本输入退格字符，文本继续为空。

    示例 1：

    输入：S = "ab#c", T = "ad#c"
    输出：true
    解释：S 和 T 都会变成 “ac”。
    示例 2：

    输入：S = "ab##", T = "c#d#"
    输出：true
    解释：S 和 T 都会变成 “”。
    示例 3：

    输入：S = "a##c", T = "#a#c"
    输出：true
    解释：S 和 T 都会变成 “c”。
    示例 4：

    输入：S = "a#c", T = "b"
    输出：false
    解释：S 会变成 “c”，但 T 仍然是 “b”。

'''
import math
class Solution:
    def cleanStr(self,s):
        '''
            方法：栈
            思路：
                遇到 非# 就 append ,否则就 pop
        '''
        stack = list()
        for c in s:
            if c!="#":
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)

    def backspaceCompare(self, S, T):
        return self.cleanStr(S)==self.cleanStr(T)

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            res = solution.backspaceCompare(str1,str2)
            print(res)
        else:
            break

