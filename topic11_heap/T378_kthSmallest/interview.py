'''
    378. 有序矩阵中第K小的元素
    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
    请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

     

    示例:

    matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ],
    k = 8,

    返回 13。

'''
import heapq
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 堆 解法
    def kthSmallest(self, matrix, k):
        print(f"matrix:{matrix}")
        minheap = []
        n = len(matrix)
        for i in range(min(k,n)):
            heapq.heappush(minheap, (matrix[i][0],i,0))

        counter = 0
        x,i,j = 0,0,0
        while counter < k:
            counter = counter + 1
            x, i, j = heapq.heappop(minheap)
            print(f"x:{x}, i:{i}, j:{j}")
            if j < n-1:
                heapq.heappush(minheap, (matrix[i][j+1],i,j+1))
        return x


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums1 = [[int(num) for num in nums.split(",") ] for nums in str1.split(";") ]
            k = int(str2)
            
            res = solution.kthSmallest(nums1,k)
            print(res)
        else:
            break

