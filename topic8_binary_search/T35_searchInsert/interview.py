'''
    35. 搜索插入位置

    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

    你可以假设数组中无重复元素。

    示例 1:

    输入: [1,3,5,6], 5
    输出: 2
    示例 2:

    输入: [1,3,5,6], 2
    输出: 1
    示例 3:

    输入: [1,3,5,6], 7
    输出: 4
    示例 4:

    输入: [1,3,5,6], 0
    输出: 0

'''
class Solution:
    def searchInsert(self, nums, target):
        nums_len = len(nums)
        if nums_len==0:
            return 0
        if nums[-1]<target:
            return nums_len
        l = 0
        r = nums_len-1
        while l<r:
            mid = l + (r-l)//2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid+1
        return l
        
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = [int(num) for num in str1.split(",")]
            target = int(str2)
            res = solution.searchInsert(nums,target)
            print(res)
        else:
            break

