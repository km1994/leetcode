'''
    394. 字符串解码
    
    给定一个经过编码的字符串，返回它解码后的字符串。

    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

    你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

    此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

    示例:

    s = "3[a]2[bc]", 返回 "aaabcbc".
    s = "3[a2[c]]", 返回 "accaccacc".
    s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

'''
import math
class Solution:
    def decodeString(self, s):
        s_stack = []
        res = ""
        count = 0
        for c in s:
            if c == "[":
                s_stack.append([count,res])
                res = ""
                count = 0
            elif c == "]":
                cur_count,last_res = s_stack.pop()
                res = last_res + cur_count*res
            elif '0'<=c<='9':
                count = count*10+int(c)
            else:
                res = res + c
        return res


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.decodeString(str1)
            print(res)
        else:
            break

