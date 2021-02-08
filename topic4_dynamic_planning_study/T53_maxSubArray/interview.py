'''
    53. 最大子序和

    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''
class Solution:
    # 动归 2
    def maxSubArray2(self, nums: List[int]) -> int:
        '''
            方法一：动态规划
                问题分析：
                    该问题 其实 可以转化 为 求 每一步 的 最大值：
                        pre_val = max(pre_val+nums[i],nums[i])

                思路：
                    对数组进行遍历，然后做以下判断：
                        1. 比较 前一步最大值+当前值 与 当前值 的大小：
                            pre_val = max(pre_val+nums[i],nums[i])
                        2. 比较当前 最大值 和 最大子序列 res 的大小：
                            res = max(res,pre_val)

        '''
        nums_len = len(nums)
        if nums_len==0:
            return 0
        pre_val = nums[0]
        res = nums[0]
        for i in range(1,nums_len):
            pre_val = nums[i] if nums[i]> pre_val+nums[i] else pre_val+nums[i]
            res = res if res>pre_val else pre_val
        return res

    # 动态规划 1
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

