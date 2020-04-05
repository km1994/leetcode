'''
    18. 四数之和

    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

    注意：

    答案中不可以包含重复的四元组。

    示例：

    给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

    满足要求的四元组集合为：
    [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
    ]

'''
class Solution:
    def fourSum(self, nums, target):
        nums_len = len(nums)
        print(f"nums_len:{nums_len}")
        if nums_len < 4:
            print(1)
            return []
        nums = sorted(nums)
        res = []
        for i in range(nums_len-3):
            print(2)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,nums_len-2):
                print(3)
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = nums_len - 1
                while l < r:
                    print(4)
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp < target:
                        l = l + 1
                    elif temp > target:
                        r = r - 1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l = l + 1
                        r = r - 1
                        while l<r and nums[l] == nums[l-1]:
                            l = l + 1
                        while l<r and nums[r] == nums[r+1]:
                            r = r - 1
        return res

   
    

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = [int(num) for num in str1.split(",")]
            target = int(str2)
            res = solution.fourSum(nums, target)
            print(res)
        else:
            break

