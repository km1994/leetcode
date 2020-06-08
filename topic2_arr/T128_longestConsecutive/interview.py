'''
    128. 最长连续序列

   给定一个未排序的整数数组，找出最长连续序列的长度。

    要求算法的时间复杂度为 O(n)。

    示例:

    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

'''
class Solution:
    def longestConsecutive1(self, nums):
        nums = sorted(nums)
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        elif nums_len == 1:
            return 1
        res = 1
        temp_count = 1
        for i in range(1,nums_len):
            if nums[i] - nums[i-1] > 1:
                temp_count = 1
            elif nums[i] - nums[i-1] == 1:
                temp_count += 1
            if temp_count>res:
                res = temp_count
        return res

    # def longestConsecutive(self, nums):
    #     res = 0
    #     if nums == []:
    #         return res
    #     nums_dict = {}
    #     for num in nums:
    #         if num-1 in nums_dict:
    #             nums_dict[num] = nums_dict[num-1]+1
    #         else:
    #             nums_dict[num] = 1
    #         if nums_dict[num]>res:
    #             res=nums_dict[num]
    #     return res


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(s) for s in str1.split(",")]
            res = solution.longestConsecutive(nums)
            print(res)
        else:
            break

