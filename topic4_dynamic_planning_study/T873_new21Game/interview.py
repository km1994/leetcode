'''
    837. 新21点
    爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

    爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

    当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

    示例 1：

    输入：N = 10, K = 1, W = 10
    输出：1.00000
    说明：爱丽丝得到一张卡，然后停止。
    示例 2：

    输入：N = 6, K = 1, W = 10
    输出：0.60000
    说明：爱丽丝得到一张卡，然后停止。
    在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
    示例 3：

    输入：N = 21, K = 17, W = 10
    输出：0.73278
    提示：

    0 <= K <= N <= 10000
    1 <= W <= 10000
    如果答案与正确答案的误差不超过 10^-5，则该答案将被视为正确答案通过。
    此问题的判断限制时间已经减少。

'''
import copy
class Solution:
    # 动态规划法
    def new21Game(self, N, K, W):
        # 先判断 K - 1 + W 是否在 N 的里面，如果在的话，说明肯定能赢得游戏，返回 1.0，也就是 100%
        if N-K+1>=W:
            return 1.0
        dp = [0.0 for _ in range(K+W)]
        # 将能赢得游戏的点数的概率设置为 1
        for i in range(K,N+1):
            dp[i] = 1.0
        # 计算 E+W 这几个点数的概率和
        sumProb = N-K+1
        # 从 K-1 开始计算
        for i in range(K-1,-1,-1):
            #点数为 i 的赢得游戏的概率 为 i+1 ~ i+W 的概率和除以 W
            dp[i] = sumProb/W
            sumProb = sumProb - dp[i+W] + dp[i]
        return dp[0]

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        if str1 != "" and str2 != "" and str3 != "":
            N = int(str1)
            K = int(str2)
            W = int(str3)
            res = solution.new21Game(N, K, W)
            print(res)
        else:
            break

