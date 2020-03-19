'''
    1. 两数之和
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):
        temp_dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in temp_dict:
                return [i,temp_dict[temp]]
            temp_dict[nums[i]] = i
        return None



if __name__ == "__main__":
    
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums,target)
    print(res)
    







        


  