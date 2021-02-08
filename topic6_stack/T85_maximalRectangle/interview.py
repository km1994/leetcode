'''
    85. 最大矩形

    给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

    示例:

    输入:
        [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
    输出: 6

'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
            参考：
                https://leetcode-cn.com/problems/maximal-rectangle/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-8/
            问题解析：
                这道题，其实可以在 84 题【求一个直方图矩形的最大面积】的延伸：
                    84 题：求 直方图矩形的最大面积
                    这道题：如果你 将 直角坐标 从上往下移动，其实就是转化为 坐标轴 从上到下                               所 构成的 直方图 的 最大面积【注：需要考虑 0 的存在问题！】
            思路：
                1. 定义 一个维度 与 矩阵 列 相等 的 数组 heights;
                2. 对 矩阵 从上往下 遍历：
                    2.1 遍历每一列：
                        若 matrix[i][j] == 1，则 heights[j] += 1 
                        若 matrix[i][j] == 0, 则 heights[j] = 0 【原因：遇到断层问题，也就是不连续 】
                    2.2 调用 84 题 方法，计算 当前坐标系 下的 直方图矩阵的最大面积
            复杂度：
                时间：O(mn)
                空间：O(n)   【原因：只 定义了 heights[] 列表】
        '''
        if len(matrix) == 0:
            return 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        heights = [0 for _ in range(col_len)]
        max_area = 0
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area,self.largestRectangleArea(heights))
        return max_area
    
    def largestRectangleArea(self,heights):
        max_area = 0
        stack = []
        p = 0
        while p<len(heights):
            if len(stack)==0:
                stack.append(p)
                p += 1
            else:
                top = stack[-1]
                if heights[p] >= heights[top]:
                    stack.append(p)
                    p += 1
                else:
                    height = heights[stack.pop()]
                    left_less_min = -1 if len(stack) ==0 else stack[-1]
                    right_less_min = p
                    area = (right_less_min-left_less_min-1)*height
                    max_area = max(area,max_area)
        while len(stack):
            height = heights[stack.pop()]
            left_less_min = -1 if len(stack) ==0 else stack[-1]
            right_less_min = len(heights)
            area = (right_less_min-left_less_min-1)*height
            max_area = max(area,max_area)
        return max_area

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            matrix= [[int(c) for c in s.split(",")] for s in str1.split(";")]
            res = solution.maximalRectangle(matrix)
            print(res)
        else:
            break

