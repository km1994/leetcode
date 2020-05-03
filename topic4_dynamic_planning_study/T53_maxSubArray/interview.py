'''
    53. 最大子序和

    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''
class Solution:
    # 动态规划
    def maxSubArray(self, nums):
        if not nums:
            return 0
        pre_num = 0
        res =0
        for num in nums:
            pre_num = max(num,pre_num+num)
            res = max(pre_num,res)
        return res
    def maxSubArray1(self, nums):
        nums_len = len(nums)
        res = nums[0]
        for i in range(1,nums_len):
            nums[i] = nums[i] if nums[i]>nums[i-1]+nums[i] else nums[i-1]+nums[i]
            res = nums[i] if nums[i]>res else res
        return res



if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.maxSubArray1(nums)
            print(res)
        else:
            break

