'''
   剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

   输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

    示例：
        输入：nums = [1,2,3,4]
        输出：[1,3,2,4] 
        注：[3,1,2,4] 也是正确的答案之一。
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        '''
            方法：双指针【与快排方法一致】
            思路：
                1. 定义 左右指针l，r；
                2. 遍历数组：
                    1. l 从 数组左边向中间遍历，直到遇到 偶数；
                    2. r 从 数组右边向中间遍历，直到遇到 奇数；
                    3. 交换 nums[l],nums[r] = nums[r],nums[l]；
                    4. l,r = l+1,r-1
        '''

        nums_len = len(nums)
        if nums_len<2:
            return nums 
        l = 0
        r = nums_len-1
        while l<r:
            while l<r and nums[l]&1==1:
                l = l+1
            while l<r and nums[r]&1==0:
                r = r-1
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        return nums

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.exchange(nums)
            print(res)
        else:
            break

