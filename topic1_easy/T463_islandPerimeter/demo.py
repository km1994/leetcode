'''
    463. 岛屿的周长

    给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

    网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

    岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

    示例 :

    输入:
    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

    输出: 16

    解释: 它的周长是下面图片中的 16 个黄色的边：



'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        row = len(grid)
        if row==0:
            return res
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1: 
                    # 下边为1，表示垂直方向非边界区
                    down = 2 if i<row-1 and grid[i+1][j]==1 else 0
                    # 右边为1，表示水平方向非边界区
                    right = 2 if j<col-1 and  grid[i][j+1]==1 else 0
                    res = res + 4 - down - right 
        return res

    # 方法一：回溯法
    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row==0:
            return 0
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return self.dfs(grid,i,j)
        return 0

    def dfs(self,grid, r,c):
        # 到达 地图边界
        if  0<=r and r<len(grid) and 0<=c and c<len(grid[0]):
            if grid[r][c]==0:
                return 1
            if grid[r][c] != 1:
                return 0
            # 用于标注 被走过的位置，防止 重复遍历
            grid[r][c] == 2
            return self.dfs(grid,r+1,c)+self.dfs(grid,r-1,c)+self.dfs(grid,r,c-1)+self.dfs(grid,r,c+1)
        else:
            return 1


if __name__ == "__main__":
    
    solution = Solution()
    matrix = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    target = 5
    res = solution.islandPerimeter(matrix,target)
    print(res)






        


  