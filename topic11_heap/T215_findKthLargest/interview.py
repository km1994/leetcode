'''
    215. 数组中的第K个最大元素
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    示例 1:

    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
'''
import heapq
import math 
class Solution:
    # 利用 队列，建立一个 数组 保存 前 k 个 数
    def findKthLargest1(self, nums, k):
        if k == 1 and len(nums) == 1:
            return nums[-1]
        res_list = [-999 for _ in range(k+1)]
        for num in nums:
            print(f"num:{num}")
            for i in range(len(res_list)-2,-1,-1):
                if res_list[i] < num:
                    res_list[i+1] = res_list[i]
                    res_list[i] = num

            print(f"res_list:{res_list}")
        return res_list[-2]

    # 堆排序 一 自己编写 堆 方法
    def findKthLargest2(self, nums, k):
        nums_len = len(nums)
        # 1.构建大顶堆
        for i in range(math.floor(nums_len/2),-1,-1):
            # 从第一个非叶子结点从下至上，从右至左调整结构
            self.adjustHeap(nums,i,nums_len)
        # 2.调整堆结构+交换堆顶元素与末尾元素
        for i in range(nums_len-1,nums_len-1-k,-1):
            # 将堆顶元素与末尾元素进行交换
            self.swap(nums,0,i)
            # 重新对堆进行调整
            self.adjustHeap(nums,0,i)
        print(nums)
        return nums[-k]
    
    def adjustHeap(self,nums,i,nums_len):
        '''
            功能：交调整大顶堆（仅是调整过程，建立在大顶堆已构建的基础上）
            @param nums        List 数组
            @param i           int  索引1
            @param nums_len    int  长度 
            @retusn
        '''
        left = 2*i+1    # i 的 左节点
        right = 2*i+2   # i 的 右节点
        largest = i     # 用于标记当前最大的节点值得索引，先取出当前元素i
        # 比较 左节点 和 当前节点 的值
        if left < nums_len and nums[left] > nums[largest]:
            largest = left
        # 比较 左节点 和 当前节点 的值
        if right<nums_len and nums[right]>nums[largest]:
            largest = right
        # 将 当前节点 和 最大节点 交换，然后重新构建 堆
        if largest!=i:
            self.swap(nums,i,largest)
            self.adjustHeap(nums,largest,nums_len)
        
    def swap(self,nums,a,b):
        '''
            功能：交换元素
            @param nums List 数组
            @param a    int  索引1
            @param b    int  索引2 
            @retusn
        '''
        nums[a],nums[b] = nums[b],nums[a]
    
    # 堆排序 二  直接 用到 系统库
    def findKthLargest3(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # 快排
    def findKthLargest4(self, nums, k):
        self.nums=nums
        self.k = k
        self.QuickSort(0,len(nums)-1)
        return self.nums[k-1]

    def AdjustPartiton(self,low,high):
        left = low
        right = high
        temp = self.nums[right]
        while left < right:
            while left < right and temp <= self.nums[left]:
                left = left + 1
            self.nums[right] = self.nums[left]
            while left < right and temp >= self.nums[right]:
                right = right - 1
            self.nums[left] =self.nums[right]
        self.nums[right] = temp

        return left

    def QuickSort(self,low,high):
        if low < high:
            pivot = self.AdjustPartiton(low,high)
            self.QuickSort(low,pivot-1)
            self.QuickSort(pivot+1,high)
    
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "" :
            nums1 = [int(num) for num in str1.split(",")]
            k = int(str2)
            res = solution.findKthLargest(nums1,k)
            print(res)
        else:
            break

