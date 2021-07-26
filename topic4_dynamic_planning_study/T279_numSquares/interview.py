class Solution(object):
    def numSquares(self, n):
        """
            方法：动态规划
            思路：
                状态方程：dp[i] = min(dp[i],dp[i-j*j]+1)
        """
        # step 1：初始化
        dp = [i for i in range(n+1)]
        # step 2：遍历
        for i in range(1,n+1):
            j = 1
            while i-j*j >= 0:
                dp[i] = min(dp[i],dp[i-j*j]+1)
                j=j+1
        return dp[-1]