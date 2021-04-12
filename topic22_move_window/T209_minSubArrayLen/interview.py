class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
            方法：滑动窗口法
        '''
        # step 1：判空
        nums_len = len(nums)
        if nums_len==0:
            return 0
        # step 2：定义左右指针
        l = 0
        r = 0
        res = nums_len+1    # res 取最大上限
        total = 0
        # step 3：滑动窗口
        while r<nums_len:
            total = total+nums[r]
            # step 4：total >= target 时，左指针需要左移，直到 total < target 
            while total>=target:
                # step 5：取最优
                res = min(res,r-l+1)       
                total = total - nums[l]
                l = l+1
            r=r+1
        return 0 if res>nums_len else res 