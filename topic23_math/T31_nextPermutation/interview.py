'''
    31. 下一个排列
    
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

    必须原地修改，只允许使用额外常数空间。

    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

'''
class Solution:
    def nextPermutation(self, nums: List[int]):
        '''
            方法一：两遍扫描【官方解】
            目标：一个大于当前序列的新序列，且变大的幅度尽可能小
            解析：

        '''
        i = len(nums) - 2
        # step 1 :从后向前 找到 第一个 满足 nums[i] < nums[i + 1] 的 i，此时 [i+1,n] 为降序序列
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # step 2 :在 [i+1,n]中，从后往前找到第一个满足 nums[i] < nums[j] 的 j，交换 nums[i]， nums[j]
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # step 3：对 [i+1,len] 做翻转
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


    def nextPermutation1(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print("origin nums:{0}".format(nums))
        n = len(nums)
        max_num = nums[-1]
        sign = True
        for i in range(2, n + 1):
            if nums[-i] < nums[-i + 1]:
                sign = False
                j = -i + 1
                while j < 0:
                    if nums[j] <= nums[-i]:
                        break
                    j += 1
                break
        if sign:
            nums.reverse()
            print("nums1:{0}".format(nums))
        else:
            nums[-i], nums[j - 1] = nums[j - 1], nums[-i]
            nums[-i + 1:] = nums[-i + 1:][::-1]
            print("nums2:{0}".format(nums))

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in nums]
            res = solution.nextPermutation(nums)
            print(res)
        else:
            break

