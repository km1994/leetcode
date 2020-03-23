'''
    152. 乘积最大子序列
    给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

    示例 1:

    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。
    示例 2:

    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
class Solution:
    def maxProduct(self, nums):
        max_val = -99999
        imax = 1
        imin = 1
        for num in nums:
            if num < 0:
                imax,imin = imin,imax
            imax = imax*num if imax*num>num else num
            imin = imin*num if imin*num<num else num
            max_val = imax if imax>max_val else max_val
        return max_val


if __name__ == "__main__":
    
    solution = Solution()
    nums = [2,3,-2,4]
    res = solution.maxProduct(nums)
    print(res)
    nums = [-2,0,-1]
    res = solution.maxProduct(nums)
    print(res)
    







        


  