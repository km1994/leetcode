'''
    堆排序
'''
import math
class Solution:
    def deapsort(self,nums):
        nums_len = len(nums)
        # 1.构建大顶堆
        for i in range(math.floor(nums_len/2),-1,-1):
            # 从第一个非叶子结点从下至上，从右至左调整结构
            self.adjustHeap(nums,i,nums_len)
        # 2.调整堆结构+交换堆顶元素与末尾元素
        for i in range(nums_len-1,0,-1):
            # 将堆顶元素与末尾元素进行交换
            self.swap(nums,0,i)
            # 重新对堆进行调整
            self.adjustHeap(nums,0,i)
        return nums
    
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


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.deapsort(nums)
            print(res)
        else:
            break

