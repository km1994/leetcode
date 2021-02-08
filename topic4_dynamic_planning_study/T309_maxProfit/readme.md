# 309. 最佳买卖股票时机含冷冻期

## 题目描述

    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    示例:

    输入: [1,2,3,0,2]
    输出: 3 
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]


## 思路介绍

### 方法一 动态规划法 

#### 基本介绍

只有卖出股票后，才会进入冷冻期；买入股票是不会进入冷冻期的。

#### 思路

1. 状态定义:

定义dp[i]表示第i天结束时的状态

- dp[i][0]: 目前持有一只股票的最大收益
- dp[i][1]: 目前不持有股票，且处于冷冻期的最大收益
- dp[i][2]: 目前不持有股票，且不处于冷冻期的最大收益

2. 转移方程

- dp[i][0]的转移来源：

  - a. 第i-1天持有股票，第i天什么都不做；
  - b. 第i-1天不持有股票且不处于冷冻期，则在第i天买入；

转移方程为：dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])

- dp[i][1]的转移来源：

  - a. 第i-1天持有股票，在第i天卖掉；

转移方程为：dp[i][1] = dp[i-1][0] + prices[i]

- dp[i][2]的转移来源：

  - a. 第i-1天不持有股票且不处于冷冻期；第i-1天不持有股票，且处于冷冻期；

转移方程为：dp[i][2] = max(dp[i-1][2], dp[i-1][1])

3. 初始状态

dp[0] = [-prices[0], 0, 0]

#### 代码

```python
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
```

#### 复杂度计算

> 时间复杂度：$O(n)$

> 空间复杂度：O(n^2)
