'''
   4. 寻找两个正序数组的中位数

   给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

    请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:

    nums1 = [1, 3]
    nums2 = [2]

    则中位数是 2.0
    示例 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    则中位数是 (2 + 3)/2 = 2.5

'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        nums_len = nums1_len+nums2_len
        left = -1
        right = -1
        aStart = 0
        bStart = 0
        for i in range(nums_len//2+1):
            left = right
            if aStart<nums1_len and (bStart>=nums2_len or nums1[aStart]<nums2[bStart]):
                right = nums1[aStart]
                aStart += 1
            else:
                right = nums2[bStart]
                bStart += 1
        if nums_len&1 == 0:
            return (left+right)/2
        else:
            return right 

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            nums2 = [int(num) for num in str2.split(",")]
            res = solution.findMedianSortedArrays(nums1,nums2)
            print(res)
        else:
            break

