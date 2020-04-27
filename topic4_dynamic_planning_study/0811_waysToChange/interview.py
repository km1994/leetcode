''' 面试题 08.11. 硬币

    硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

    示例1:

    输入: n = 5
    输出：2
    解释: 有两种方式可以凑成总金额:
    5=5
    5=1+1+1+1+1
    示例2:

    输入: n = 10
    输出：4
    解释: 有四种方式可以凑成总金额:
    10=10
    10=5+5
    10=5+1+1+1+1+1
    10=1+1+1+1+1+1+1+1+1+1
'''
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    '''
        方法三 动态规划
    '''
    def waysToChange(self, n):
        '''
            动态规划
            :param coins: List
            :param amount: int
            :return:
                ans  int
        '''
        mod = 10**9 + 7
        dp = [0] * (n+1)
        coins = [1,5,10,25]
        dp[0] = 1
        for coin in coins:
            for i in range(coin,n+1):
                dp[i] = dp[i] + dp[i-coin]
        print(f"dp:{dp}")
        return dp[-1] % mod

if __name__ == "__main__":

    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            num = int(str1)
            res = solution.waysToChange(num)
            print(res)
        else:
            break

   