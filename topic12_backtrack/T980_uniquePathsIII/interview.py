'''
    980. 不同路径 III
    在二维网格 grid 上，有 4 种类型的方格：

    1 表示起始方格。且只有一个起始方格。
    2 表示结束方格，且只有一个结束方格。
    0 表示我们可以走过的空方格。
    -1 表示我们无法跨越的障碍。
    返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

     

    示例 1：

    输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    输出：2
    解释：我们有以下两条路径：
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
    示例 2：

    输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    输出：4
    解释：我们有以下四条路径： 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
    示例 3：

    输入：[[0,1],[2,0]]
    输出：0
    解释：
    没有一条路能完全穿过每一个空的方格一次。
    请注意，起始和结束方格可以位于网格中的任意位置。

'''
import copy
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def uniquePathsIII(self, grid):
        self.res = 0
        row = len(grid)
        if row == 0:
            return res
        col = len(grid[0])
        zero_count = 0
        x = 0
        y = 0
        def backtrack(grid,zero_count,i,j,row,col):
            '''
                功能： 回溯函数
                @param grid        List(n*m)   字符二维网络
                @param zero_count  int         0 
                @param i            int         当前行
                @param j            int         当前列
                @param row            int       行数
                @param col            int       列数
                return
                    
            '''
            # 判断是否越界
            if i>=row or i < 0 or j>=col or j<0:
                return 
            # 判断是否遇到障碍，需要返回
            if grid[i][j]==-1:
                return 
            # 到达终点，但是未走完所有空格
            if grid[i][j]==2 and zero_count!=0:
                return 
            # 到达终点，走完所有空格
            if grid[i][j]==2 and zero_count==0:
                self.res = self.res+1
                return 
            temp = grid[i][j]
            grid[i][j] = -1
            backtrack(grid,zero_count-1,i-1,j,row,col)
            backtrack(grid,zero_count-1,i+1,j,row,col)
            backtrack(grid,zero_count-1,i,j-1,row,col)
            backtrack(grid,zero_count-1,i,j+1,row,col)
            grid[i][j] = temp
            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    x = i
                    y = j
                    zero_count = zero_count+1
                elif grid[i][j] == 0:
                    zero_count = zero_count+1
        backtrack(grid,zero_count,x,y,row,col)
        return self.res


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            board = [[int(c) for c in s.split(",")] for s in str1.split(";")]
            print(f"board:{board}")

            res = solution.uniquePathsIII(board)
            print(res)
        else:
            break

