'''
    62. 不同路径

    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

    示例 1:

    输入:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右

'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
            功能：动态规划
            input:
                obstacleGridm list 网格
            output:
                dp[m-1][n-1] int 到达 终点 的 方法数
        '''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] else 0

        for i in range(1,n):
            obstacleGrid[0][i] = 1 if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] else 0

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
        


if __name__ == "__main__":
    solution = Solution()
    print("---------------1----------------")
    obstacleGrid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print("res:{0}".format(res))

    print("---------------2----------------")
    obstacleGrid =[[1]]
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print("res:{0}".format(res))

    print("---------------3----------------")
    obstacleGrid =[[0,1]]
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print("res:{0}".format(res))

    print("---------------4----------------")
    obstacleGrid =[[0,0],[1,1],[0,0]]
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print("res:{0}".format(res))





        


  