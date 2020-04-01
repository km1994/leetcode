'''
    150. 逆波兰表达式求值
    
    根据逆波兰表示法，求表达式的值。

    有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

    说明：

    整数除法只保留整数部分。
    给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
    示例 1：

        输入: ["2", "1", "+", "3", "*"]
        输出: 9
        解释: ((2 + 1) * 3) = 9
    示例 2：

        输入: ["4", "13", "5", "/", "+"]
        输出: 6
        解释: (4 + (13 / 5)) = 6
    示例 3：

        输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        输出: 22
        解释: 
        ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22

'''
import math
class Solution:
    def evalRPN1(self, tokens):
        stack = []
        symbol = ["+","-","*","/"]
        for token in tokens:
            if token not in symbol:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    stack.append(str(a+b))
                elif token == '-':
                    stack.append(str(a-b))
                elif token == '*':
                    stack.append(str(a*b))
                elif token == '/':
                    stack.append(str(int(a/b)))
        return int(stack[0])

    def evalRPN(self, tokens):
        stack = []
        symbol_dict = {
            "*": lambda x,y: x * y,
            r"/": lambda x,y: int(y/x),
            "+": lambda x,y: x + y,
            "-": lambda x,y: y - x
        }
        for token in tokens:
            if token not in symbol_dict:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(symbol_dict[token](a,b))
        return int(stack[0])



if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            tokens = str1.split(",")
            res = solution.evalRPN(tokens)
            print(res)
        else:
            break

