#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: findKthLargest.py
@time: 2019/8/05
@rel： https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
@url：
@desc:
    215. 数组中的第K个最大元素

    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    示例 1:

    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

'''

class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

    def findKthLargest1(self, nums, k):
        if len(nums) < k:
            return
        sort_list = [-999] * k

        for i in range(0,len(nums)):
            for j in range(0,k):
                if nums[i] > sort_list[j]:
                    n = k - 1
                    while n > j:
                        sort_list[n] = sort_list[n-1]
                        n = n - 1
                    sort_list[n] = nums[i]
                    break
        #     print("sort_list:{0}".format(sort_list))
        # print("sort_list:{0}".format(sort_list))
        print("sort_list[-1]:{0}".format(sort_list[-1]))
        return sort_list[-1]

    def findKthLargest2(self, nums, k):
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

    # 最小堆下沉法
    def down(self,parent,heap):
        n = len(heap)

        child = parent * 2 + 1
        if child >= n:
            return 

        # 如果存在另一个子节点，且其比第一个还小，则改成以其左参考
        if child+1 < n and heap[child+1] < heap[child]:
            child = child + 1

        if heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            # 如果产生了替换，则继续从被替换的位置往下尝试，直到原parent的元素下沉到不可再下沉为止
            self.down(child, heap)

    def findKthLargest(self, nums, k):
        n =len(nums)
        heap = nums[:k]
        # 例如 3, 2, 3, 1, 2, 4, 5, 5, 6，找第4个最大
	    # 则前4个位置做最小堆
        last = k - 1
        # 做最小堆的原理是从最下面的元素开始做，每次往前塞一个元素，然后尝试下沉
        # 所以从最下层的子节点还去尝试下沉没有任何意义

        # 因为最小堆的特性 parent*2+1=first child、parent*2+2=second child
        # 倘若某一个节点是某个父节点的第二个节点，则 (child-2)/2 即为其父节点的位置
        # 倘若某一个节点是某个父节点的第一个节点，则 (child-1)/2 即为其父节点的位置
        # 而在不考虑余数的情况下 我们可以发现一般第二个节点的位置 2,4,6... 也适用于 (child-1)/2
        # 所以利用此特性 (child-1)/2 也能直接找到某元素在堆里的父节点

        # 所以我们从 (last - 1) / 2 开始往前推即可，此位置必定是最后一个带有子节点的父节点位置
        # 其实不判断也差别不大，down方法肯定也要去判断
        for p in range(int((last-1)/2),-1,-1):
            self.down(p,heap)
        # 将k之后位置的元素不断和前k个里最小元素比较，即最小堆的根节点比较
        for i in range(k,n):
            # 如果有数大于最小堆中最小
		    # 则需要将两者调换之后尝试下沉即可
            if nums[i]>heap[0]:
                heap[0] = nums[i]
                self.down(0,heap)

        return heap[0]




if __name__ == "__main__":
    # nums = [3,2,1,5,6,4]
    # k = 2
    # solution =Solution()
    # solution.findKthLargest(nums,k)

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    solution = Solution()
    res = solution.findKthLargest(nums, k)

    print("res:{0}".format(res))

    
