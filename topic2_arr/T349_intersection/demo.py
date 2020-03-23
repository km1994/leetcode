'''
    349. 两个数组的交集
    给定两个数组，编写一个函数来计算它们的交集。

    示例 1:

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2]
    示例 2:

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [9,4]

'''
class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        new_nums = []

        for num1 in nums1:
            if num1 in nums2:
                new_nums.append(num1)
        return new_nums
        


if __name__ == "__main__":
    
    solution = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = solution.intersection(nums1,nums2)
    print(res)

    







        


  