'''
    309. 最佳买卖股票时机含冷冻期
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    示例:

    输入: [1,2,3,0,2]
    输出: 3 
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

'''
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 动态规划法 采用列表法
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [[0]*3 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2],dp[i-1][1])
        return max(dp[-1])
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            num1 = [int(c) for c in str1.split(",")]
            res = solution.maxProfit(num1)
            print(res)
        else:
            break

