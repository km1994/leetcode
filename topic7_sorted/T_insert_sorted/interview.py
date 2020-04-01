'''
    实现插入排序算法？

'''
class Solution:
    def insert_sorted(self, nums):
        nums = [int(num) for num in nums]
        nums_len = len(nums)
        for i in range(nums_len):
            max_num = nums[i]
            for j in range(i+1,nums_len):
                if nums[j] > max_num:
                    nums[j],max_num = max_num,nums[j]
            nums[i] = max_num
        return nums

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = str1.split(",")
            res = solution.insert_sorted(nums)
            print(res)
        else:
            break

