'''
    200. 岛屿数量
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

    此外，你可以假设该网格的四条边均被水包围。

    示例 1:

    输入:
    11110
    11010
    11000
    00000
    输出: 1
    示例 2:

    输入:
    11000
    11000
    00100
    00011
    输出: 3
    解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

'''
import collections
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def numIslands1(self, grid):
        def backtrack(grid,i,j):
            grid[i][j] = 0
            near_list = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for x,y in near_list:
                if 0<=x<self.row and 0<=y<self.col and grid[x][y] == '1':
                    backtrack(grid,x,y)


        self.row = len(grid)
        if self.row == 0:
            return 0
        self.col = len(grid[0])
        lands_num = 0
        for r in range(self.row):
            for c in range(self.col):
                if grid[r][c] == "1":
                    lands_num = lands_num + 1
                    backtrack(grid,r,c)
        return lands_num

    # 广度遍历
    def numIslands(self, grid):
        self.row = len(grid)
        if self.row == 0:
            return 0
        self.col = len(grid[0])
        lands_num = 0
        for r in range(self.row):
            for c in range(self.col):
                if grid[r][c] == "1":
                    lands_num = lands_num + 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row,col = neighbors.popleft()
                        near_list = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
                        for x,y in near_list:
                            if 0<=x<self.row and 0<=y<self.col and grid[x][y] == '1':
                                neighbors.append((x,y))
                                grid[x][y] = "0"
        return lands_num



        



                    


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            board = [[c for c in s.split(",")] for s in str1.split(";")]
            print(f"board:{board}")

            res = solution.numIslands(board)
            print(res)
        else:
            break

