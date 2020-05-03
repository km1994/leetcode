'''
    300. 最长上升子序列

    给定一个无序的整数数组，找到其中最长上升子序列的长度。

    示例:

    输入: [10,9,2,5,3,7,101,18]
    输出: 4 
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
    说明:

    可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
    你算法的时间复杂度应该为 O(n2) 。

'''
class Solution:
    def lengthOfLIS(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        res = 1
        dp = [1]*nums_len
        for i in range(nums_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
                    res = max(dp[i],res)
        print(f"res:{res}")
        return res
            
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.lengthOfLIS(nums)
            print(res)
        else:
            break

