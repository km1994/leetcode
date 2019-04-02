'''
	给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

    你可以假设 nums1 和 nums2 不会同时为空。

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
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        res = nums1
        if not res: 
            return None
        res.sort()
        l = len(res)
        if l % 2:
            return res[int(l/2)] / 1.0 
        else : 
            return (res[int(l/2)] + res[int(l/2)-1]) / 2.0

if __name__ == "__main__":
    nums1=[1,2,6]
    nums2=[2,3,4]
    solution = Solution()
    median=solution.findMedianSortedArrays(nums1,nums2)
    print(f"median:{median}")
  