'''
    350. 两个数组的交集 II
    给定两个数组，编写一个函数来计算它们的交集。

    示例 1:

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2,2]
    示例 2:

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [4,9]
    说明：

    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
    我们可以不考虑输出结果的顺序。

'''
class Solution:
    def intersect(self, nums1, nums2):
        new_nums = []
        
        for num1 in nums1:
            if num1 in nums2:
                new_nums.append(num1)
                nums2.remove(num1)
        return new_nums


if __name__ == "__main__":
    
    solution = Solution()
    print("-----------1-----------")
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = solution.intersect(nums1,nums2)
    print(res)

    print("-----------2-----------")
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = solution.intersect(nums1,nums2)
    print(res)

    


    







        


  