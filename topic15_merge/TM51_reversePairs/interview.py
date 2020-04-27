'''
    面试题51. 数组中的逆序对

    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

    示例 1:

    输入: [7,5,6,4]
    输出: 5   

    限制：

    0 <= 数组长度 <= 50000

'''
class Solution:
    def reversePairs(self, nums):
        nums_len = len(nums)
        nums_temp = [0]*nums_len
        return self.mergeSort(nums,nums_temp,0,nums_len-1)

    def mergeSort(self,nums,nums_temp,l,r):
        if l>=r:
            return 0

        mid = (l+r)//2
        inv_count = self.mergeSort(nums,nums_temp,l,mid) + self.mergeSort(nums,nums_temp,mid+1,r)
        i = l
        j = mid+1
        pos = l
        # 归并
        while i<=mid and j<=r:
            if nums[i] <= nums[j]:
                nums_temp[pos] = nums[i]
                i = i+1
                inv_count = inv_count + (j-(mid+1))
            else:
                nums_temp[pos] = nums[j]
                j = j + 1
            pos = pos + 1
        # 将左边剩余元素加入 nums_temp
        for k in range(i,mid+1):
            nums_temp[pos] = nums[k]
            inv_count = inv_count + (j-(mid+1))
            pos = pos + 1
        # 将右边剩余元素加入 nums_temp
        for k in range(j,r+1):
            nums_temp[pos] = nums[k]
            pos = pos + 1
        nums[l:r+1] = nums_temp[l:r+1]
        return inv_count

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.reversePairs(nums)
            print(res)
        else:
            break

