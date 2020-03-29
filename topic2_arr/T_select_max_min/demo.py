'''
    在一个未排序的整型数组中，如何找到最大和最小的数字？

'''
class Solution:
    def select_max_min(self, nums):
        max_val = nums[0]
        min_val = nums[0]
        for num in nums:
            if max_val < num:
                max_val = num
            elif min_val > num:
                min_val = num
        return [max_val,min_val]


    
if __name__ == "__main__":
    
    solution = Solution()
    print("-----------1-----------")
    nums = [1,5,7,3]
    res = solution.select_max_min(nums)
    print(res)

    print("-----------2-----------")
    nums = [1]
    res = solution.select_max_min(nums)
    print(res)

    print("-----------3-----------")
    nums = [1,0,4,1,5,1,6,0]
    res = solution.select_max_min(nums)
    print(res)


    


    







        


  