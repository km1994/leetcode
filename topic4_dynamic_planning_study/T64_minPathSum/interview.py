'''
    416. 分割等和子集

    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

    注意:

    每个数组中的元素不会超过 100
    数组的大小不会超过 200
    示例 1:

    输入: [1, 5, 11, 5]

    输出: true

    解释: 数组可以分割成 [1, 5, 5] 和 [11].
     

    示例 2:

    输入: [1, 2, 3, 5]

    输出: false

    解释: 数组不能分割成两个元素和相等的子集.

'''
class Solution:
    # 动态规划
    def canPartition(self, nums):
        nums_len = len(nums)
        # 数组长度 为空
        if nums_len==0:
            return False
        # 数组求和
        sum_val = 0
        for num in nums:
            sum_val = sum_val+num
        # 如果 数组之和 为 奇数，说明不可能找到妹子要求的两个子列表
        if sum_val&1==1:
            return False
        # 是否可以从给定的数组中挑出一些数，这些数的总和恰好是数组总和的一半
        target = int(sum_val/2)

        dp = [False for _ in range(target+1)]

        dp[0] = True
        for i in range(1,nums_len):
            for j in range(target,nums[i]-1,-1):
                if dp[target]:
                    return True
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target]
        

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.canPartition(nums)
            print(res)
        else:
            break

