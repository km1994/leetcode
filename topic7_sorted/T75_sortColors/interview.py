class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        题目：75.颜色分类
        """
        left,cur = 0,0
        right = len(nums)-1
        while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left] = nums[left],nums[cur]
                cur = cur+1
                left = left+1
            elif nums[cur]==2:
                nums[cur],nums[right] = nums[right],nums[cur]
                right = right-1
            else:
                cur = cur+1