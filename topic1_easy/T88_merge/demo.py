'''
    88. 合并两个有序数组

    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

    说明:

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    
    示例:

    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    输出: [1,2,2,3,5,6]
'''
class Solution:
    def merge(self, nums1, m, nums2, n) :
        final_pos = len(nums1) - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[final_pos] = nums1[m]
                m = m - 1
            else:
                nums1[final_pos] = nums2[n]
                n = n - 1
            final_pos = final_pos - 1
        while n >= 0:
            nums1[final_pos] = nums2[n]
            n = n - 1
            final_pos = final_pos - 1

        print(f"nums1:{nums1}")
        


if __name__ == "__main__":
    
    solution = Solution()
    print("--------1-------")
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]     
    n = 3
    res = solution.merge(nums1, m, nums2, n)
    print(res)

    print("--------2-------")
    nums1 = [1,2,0,0,0]
    m = 2
    nums2 = [2,5,6]     
    n = 3
    res = solution.merge(nums1, m, nums2, n)
    print(res)

    print("--------3-------")
    nums1 = [0]
    m = 0
    nums2 = [1]     
    n = 1
    res = solution.merge(nums1, m, nums2, n)
    print(res)







        


  