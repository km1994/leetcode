#  332. 重新安排行程

## 题目描述

    给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

    说明:

    如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
    所有的机场都用三个大写字母表示（机场代码）。
    假定所有机票至少存在一种合理的行程。
    示例 1:

    输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
    示例 2:

    输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。

## 思路介绍

### 方法一：邻接表+回溯法

#### 思路

1. 构建邻接矩阵 ticketsDict；
2. 对 邻接矩阵 进行 排序（原因：题目要求按字符自然排序返回最小的行程组合）；
3. 回溯法

#### 代码

```python
class Solution:
    # 回溯法
    def findItinerary(self, tickets):
        '''
            思路：
                1. 构建邻接矩阵 ticketsDict；
                2. 对 邻接矩阵 进行 排序（原因：题目要求按字符自然排序返回最小的行程组合）；
                3. 回溯法
        '''
        if len(tickets)==0:
            return []
        ticketsDict = {}
        for ticket in tickets:
            if ticket[0] not in ticketsDict:
                ticketsDict[ticket[0]] = []
            ticketsDict[ticket[0]].append(ticket[1])
        for key,val in ticketsDict.items():
            ticketsDict[key] = sorted(val)
        res = []
        def backtrack(ticket):
            while ticket in ticketsDict and ticketsDict[ticket]:
                backtrack(ticketsDict[ticket].pop(0))
            res.insert(0,ticket)
        
        backtrack("JFK")
        return res

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            tickets = [s.split(",") for s in str1.split(";")]
            res = solution.findItinerary(tickets)
            print(res)
        else:
            break
```

#### 复杂度计算

> 时间复杂度： 
> 
> 空间复杂度： 

