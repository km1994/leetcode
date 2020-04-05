'''
    15. 三数之和

    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    示例：

        给定数组 nums = [-1, 0, 1, 2, -1, -4]，

        满足要求的三元组集合为：
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]

'''
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i + 1
                r = len(nums) - 1
                while l<r:
                    s = nums[i] + nums[l] + nums[r]
                    if s==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l = l + 1
                        r = r - 1
                        while l<r and nums[l] == nums[l-1]:
                            l = l + 1
                        while l<r and nums[r] == nums[r+1]:
                            r = r - 1
                    elif s > 0:
                        r = r - 1
                    else:
                        l = l + 1
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.threeSum(nums)
            print(res)
        else:
            break

