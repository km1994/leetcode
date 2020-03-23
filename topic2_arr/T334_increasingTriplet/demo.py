'''
    334. 递增的三元子序列
    给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

    数学表达式如下:

    如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
    使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
    说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

    示例 1:

    输入: [1,2,3,4,5]
    输出: true
    示例 2:

    输入: [5,4,3,2,1]
    输出: false

'''
class Solution:
    def increasingTriplet(self, nums):
        nums_len = len(nums)
        if nums_len<3:
            return False
        small = 99999999999999
        mid = 99999999999999
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False


        


if __name__ == "__main__":
    
    solution = Solution()
    print("-----------1-----------")
    nums = [1,2,3,4,5]
    res = solution.increasingTriplet(nums)
    print(res)

    print("-----------2-----------")
    nums = [5,4,3,2,1]
    res = solution.increasingTriplet(nums)
    print(res)

    print("-----------3-----------")
    nums = [0,4,2,1,0,-1,-3]
    res = solution.increasingTriplet(nums)
    print(res)
    
    


    







        


  