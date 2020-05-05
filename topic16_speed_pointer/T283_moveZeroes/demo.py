'''
    283. 移动零
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    示例:

    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
    说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
'''
class Solution:
    def moveZeroes(self, nums):
        nums_len = len(nums)
        if nums_len > 1:
            p = 0
            for i in range(nums_len):
                if nums[i] != 0:
                    nums[p] = nums[i]
                    p = p+1
            for i in range(p,nums_len):
                nums[i] = 0
        return nums
        


if __name__ == "__main__":
    
    solution = Solution()
    nums = [0,1,0,3,12]
    res = solution.moveZeroes(nums)
    print(res)

    







        


  