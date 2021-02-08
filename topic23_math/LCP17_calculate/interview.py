'''
    LCP 17. 速算机器人
    
    小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作 x 和 y），请小扣说出计算指令：

    "A" 运算：使 x = 2 * x + y；
    "B" 运算：使 y = 2 * y + x。
    在本次游戏中，店家说出的数字为 x = 1 和 y = 0，小扣说出的计算指令记作仅由大写字母 A、B 组成的字符串 s，字符串中字符的顺序表示计算顺序，请返回最终 x 与 y 的和为多少。

    示例 1：

    输入：s = "AB"

    输出：4

    解释：
    经过一次 A 运算后，x = 2, y = 0。
    再经过一次 B 运算，x = 2, y = 2。
    最终 x 与 y 之和为 4。

'''
class Solution:
    def calculate(self, s: str) -> int:
        funA = lambda x,y:2*x+y
        funB = lambda x,y:2*y+x
        funC = lambda x,y:x+y
        x = 1
        y = 0
        for c in s:
            if c=="A":
                x=funA(x,y)
            elif c=="B":
                y=funB(x,y)
        return funC(x,y)

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.calculate(str1)
            print(res)
        else:
            break

