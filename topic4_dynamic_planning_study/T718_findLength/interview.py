'''
    718. 最长重复子数组

    给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

    示例 1:

    输入:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    输出: 3
    解释: 
    长度最长的公共子数组是 [3, 2, 1]。
    说明:

    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100

'''
class Solution:
    # 动态规划
    def findLength(self, A, B):
        A_len = len(A)
        B_len = len(B)
        dp = [[0]*(B_len+1) for _ in range(A_len+1)]
        res = 0
        for i in range(A_len-1,-1,-1):
            for j in range(B_len-1,-1,-1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i]==B[j] else 0
                res = max(res,dp[i][j])
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            A = [int(num) for num in str1.split(",")]
            B = [int(num) for num in str2.split(",")]
            res = solution.findLength(A, B)
            print(res)
        else:
            break

