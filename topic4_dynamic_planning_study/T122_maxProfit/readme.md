# 122. 买卖股票的最佳时机 II

## 题目描述

    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:

    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
         随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
    示例 2:

    输入: [1,2,3,4,5]
    输出: 4
    解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
         注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
         因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    示例 3:

    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


## 思路介绍

### 动态规划————是和否问题

#### 解析：

该题的核心 需要 记录，第 i 天交易后的情况：

1. 没有股票的最大利润
2. 有一只股票的最大利润
   
#### ：

动态规划的转移方程：

 1. 没有股票的最大利润 ：noHas = max(notHas,has+prices[i])
 2. 有一只股票的最大利润： max(has,notHas-prices[i])

#### 代码

```python
class Solution:
    def maxProfit(self, prices):
        '''
            思路：动态规划————是和否问题
            解析：
                该题的核心 需要 记录，第 i 天交易后的情况：
                    1. 没有股票的最大利润
                    2. 有一只股票的最大利润
            思路：
                动态规划的转移方程：
                    1. 没有股票的最大利润 ：noHas = max(notHas,has+prices[i])
                    2. 有一只股票的最大利润： max(has,notHas-prices[i])
        '''
        prices_len = len(prices)
        notHas = 0
        has = -prices[0]
        for i in range(1,prices_len):
            notHas,has = max(notHas,has+prices[i]),max(has,notHas-prices[i])
            print(f"notHas:{notHas}")
            print(f"has:{has}")
        return notHas

    def maxProfit1(self, prices) :
        profit_max = 0
        i = 0
        prices_len = len(prices)
        while i < prices_len-1:
            while i < prices_len-1:
                if prices[i] > prices[i+1]:
                    i = i + 1
                else:
                    break
            j = i + 1
            while j < prices_len-1:
                if prices[j] < prices[j+1]:
                    j = j + 1
                else:
                    break
                    
            if j > prices_len - 1:
                break
            profit_max = profit_max + (prices[j]-prices[i])
            i = j + 1

        return profit_max

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

> 空间复杂度：O(n)
