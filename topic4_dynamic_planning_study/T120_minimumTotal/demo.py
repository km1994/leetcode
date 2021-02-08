'''
    120. 三角形最小路径和
    
    给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

    相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

    例如，给定三角形：

    [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
'''
class Solution:
    def minimumTotal(self, triangle):
        triangle_len = len(triangle)
        dp = [[0]*triangle_len for _ in range(triangle_len)]
        dp[0][0] = triangle[0][0]
        for i in range(1,triangle_len):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
            dp[i][i] = dp[i-1][i-1]+triangle[i][i]
        return min(dp[triangle_len-1])
        

if __name__ == "__main__":

    solution = Solution()
    print("---------------1----------------")
    nums = [
                [2],
                [3,4],
                [6,5,7],
                [4,1,8,3]
            ]
    res = solution.minimumTotal(nums)  
    print("res:{0}".format(res))

   