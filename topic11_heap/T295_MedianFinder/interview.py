'''
    295. 数据流的中位数
    中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

    例如，

    [2,3,4] 的中位数是 3

    [2,3] 的中位数是 (2 + 3) / 2 = 2.5

    设计一个支持以下两种操作的数据结构：

    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。
    示例：

    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3) 
    findMedian() -> 2

'''
import sys
sys.path.append("..") # 这句是为了导入_config
import heapq
from T_HeapSort.Heap import MaxHeap,MinHeap
class MedianFinder:

    def __init2__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.nums = []
        self.maxHeap = MaxHeap()

    def addNum1(self, num: int) -> None:
        self.nums.append(num)
        self.count = self.count + 1
        
    def findMedian1(self) -> float:
        self.max_heap = self.maxHeap.deapsort(self.nums)
        print(f"self.max_heap:{self.max_heap}")
        if self.count%2 == 1:
            return self.max_heap[int(self.count/2)]
        else:
            return (self.max_heap[int(self.count/2)-1]+self.max_heap[int(self.count/2)])/2

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):# 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]


if __name__ == "__main__":
    
    solution = MedianFinder()
    while 1:
        str1 = input()
        if str1 != "" :
            nums1 = int(str1)
            solution.addNum(nums1)
            res = solution.findMedian()
            print(res)
        else:
            break

