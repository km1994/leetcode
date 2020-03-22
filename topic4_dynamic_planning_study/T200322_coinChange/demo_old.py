''' 凑零钱问题

    给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，
    再给一个总金额 n，问你最少需要几枚硬币凑出这个金额，
    如果不可能凑出，则回答 -1 。
    
    比如说，k = 3，面值分别为 1，2，5，总金额 n = 11，
    那么最少需要 3 枚硬币，即 11 = 5 + 5 + 1 。
'''
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    '''
        方法一 递归法
    '''
    # 功能： 递归法
    def coinChange1(self, coins,amount):
        '''
        递归法
        :param n: int
        :return:
            ans  int
        '''
        if amount == 0:
            return 0
        ans = 1000000
        for coin in coins:
            if amount - coin < 0:
                continue
            subProb = self.coinChange1(coins,amount-coin)

            # 子问题无解
            if subProb == -1:
                continue
            ans = min(ans,subProb+1)
        if ans == 1000000:
            return -1
        else:
            return ans

    '''
        方法二 带有备忘录地递归法
    '''
    # 功能： 带有备忘录地递归法
    def coinChange2(self, coins,amount):
        '''
        带有备忘录地递归法
        :param n: int
        :return:
            ans  int
        '''
        # 备忘录初始值为 -2
        meno = [-2] * (amount+1)
        return self.helper(coins,amount,meno)


    def helper(self,coins,amount,meno):
        if amount == 0:
            return 0
        if meno[amount] != -2:
            return meno[amount]
        ans = 100000
        for coin in coins:
            # 金额不可达
            if amount - coin < 0:
                continue
            subProb = self.helper(coins,amount-coin,meno)
            # 子问题无解
            if subProb == -1:
                continue
            ans = min(ans,subProb+1)
        if ans == 100000:
            meno[amount] = -1
        else:
            meno[amount] = ans
        return meno[amount]

    '''
        方法三 动态规划
    '''
    # 功能： 动态规划
    def coinChange3(self, coins,amount):
        '''
        动态规划
        :param n: int
        :return:
            ans  int
        '''
        dp = [amount+1] *(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i],1+dp[i-coin])

        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]


if __name__ == "__main__":

    solution = Solution()
    print("---------------1----------------")
    coins = [1,2,5]
    amount = 11
    res = solution.coinChange1(coins,amount)
    print("res:{0}".format(res))

    print("---------------2----------------")
    coins = [1,2,5]
    amount = 11
    res = solution.coinChange2(coins,amount)
    print("res:{0}".format(res))

    print("---------------3----------------")
    coins = [1,2,5]
    amount = 11
    res = solution.coinChange3(coins,amount)
    print("res:{0}".format(res))

   