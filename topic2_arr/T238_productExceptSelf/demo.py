'''
    238. 除自身以外数组的乘积
    给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

    示例:

    输入: [1,2,3,4]
    输出: [24,12,8,6]


'''
class Solution:
    def productExceptSelf(self, nums):
        nums_len = len(nums)
        res = [1 for _ in range(nums_len)]
        left = 1                      # left：从左边累乘
        right = 1                     # right：从右边累乘
        for i in range(nums_len):     # 最终每个元素其左右乘积进行相乘得出结果
            res[i] = res[i] * left      # 乘以其左边的乘积
            left = left * nums[i]

            res[nums_len-1-i] *= right  # 乘以其右边的乘积
            right *= nums[nums_len-1-i]
        return res

    def productExceptSelf1(self, nums):
        nums_len = len(nums)
        answer = [0]*nums_len

        answer[0] = 1
        for i in range(1,nums_len):
            answer[i] = nums[i-1] * answer[i-1]
            
        R = 1
        for i in reversed(range(nums_len)):
            answer[i] = answer[i] * R
            R = R * nums[i]
        return answer

        
if __name__ == "__main__":
    
    solution = Solution()
    print("-----------1-----------")
    nums = [1,2,3,4]
    res = solution.productExceptSelf1(nums)
    print(res)

    


    







        


  