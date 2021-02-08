'''
    面试题 08.01. 三步问题

    三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

    示例1:

    输入：n = 3 
    输出：4
    说明: 有四种走法
    示例2:

    输入：n = 5
    输出：13

'''
class Solution:
    def waysToStep(self, n: int) -> int:
        '''
            解析：
                因为该孩子 只能走 1阶、2阶或3阶，所以表示 该孩子 走下一步的 方式 是 前面三种的总和

            思路：
                one,two,three = two,three,(one+two+three)%1000000007
        '''
        res = 0
        one = 1
        two = 2
        three = 4
        if n<=0:
            return res
        elif n<=1:
            return one
        elif n<=2:
            return two
        elif n<=3:
            return three
        
        for i in range(4,n+1):
            one,two,three = two,three,(one+two+three)%1000000007
        return three


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            num = int(str1)
            res = solution.waysToStep(num)
            print(res)
        else:
            break

