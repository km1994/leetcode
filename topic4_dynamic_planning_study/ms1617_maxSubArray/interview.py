class Solution(object):
    def maxSubArray(self, nums):
        """
            方法：动态规划
        """
        # step 1：判空
        nums_len = len(nums)
        if nums_len==0:
            return 0

        res = -9999999999    
        pre = 0
        # step 2：遍历数组
        for i in range(nums_len):
            # step 3：取 pre+nums[i],nums[i] 最大值
            pre = max(pre+nums[i],nums[i])
            # step 4：记录 最大的连续数列 最大值
            if pre >res:
                res = pre 
        return res