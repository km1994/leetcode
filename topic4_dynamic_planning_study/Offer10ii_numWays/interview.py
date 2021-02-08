''' 剑指 Offer 10- II. 青蛙跳台阶问题

    一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    示例 1：

    输入：n = 2
    输出：2
    示例 2：

    输入：n = 7
    输出：21
    示例 3：

    输入：n = 0
    输出：1

'''
class Solution:
    def numWays(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        p = 1
        q = 1
        for _ in range(1,n):
            tmp = p
            p = q
            q = tmp+p
        return q% 1000000007

if __name__ == "__main__":

    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            num = int(str1)
            res = solution.numWays(num)
            print(res)
        else:
            break

   