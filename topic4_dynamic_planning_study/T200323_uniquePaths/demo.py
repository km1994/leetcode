'''
    62. 不同路径

    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

    问总共有多少条不同的路径？

    示例 1:

    输入: m = 3, n = 2
    输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右

    示例 2:

    输入: m = 7, n = 3
    输出: 28

'''
class Solution:
    def uniquePaths(self, m, n):
        '''
            功能：动态规划
            input:
                m int 行
                n int 列
            output:
                dp[m-1][n-1] int 到达 终点 的 方法数
        '''
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePaths1(self, m, n):
        col = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                col[j] = col[j] + col[j-1]
        return col[-1]


if __name__ == "__main__":
    solution = Solution()
    print("---------------1----------------")
    m = 3
    n = 2
    res = solution.uniquePaths(m, n)
    print("res:{0}".format(res))
    res = solution.uniquePaths1(m, n)
    print("res:{0}".format(res))





        


  