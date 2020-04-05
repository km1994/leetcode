'''
    162. 寻找峰值

    峰值元素是指其值大于左右相邻值的元素。

    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

    数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

    你可以假设 nums[-1] = nums[n] = -∞。

    示例 1:

    输入: nums = [1,2,3,1]
    输出: 2
    解释: 3 是峰值元素，你的函数应该返回其索引 2。
    示例 2:

    输入: nums = [1,2,1,3,5,6,4]
    输出: 1 或 5 
    解释: 你的函数可以返回索引 1，其峰值元素为 2；
         或者返回索引 5， 其峰值元素为 6。

'''
class Solution:

    def findPeakElement(self, nums):
        l = 0
        r = len(nums)-1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l 

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = str1.split(",")
            res = solution.findPeakElement(nums)
            print(res)
        else:
            break

