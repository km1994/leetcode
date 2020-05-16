'''
   560. 和为K的子数组

   给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

    示例 1 :

    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :

    数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。


'''
class Solution:

    # 字典法
    def subarraySum(self, nums, k):
        num_len = len(nums)
        if num_len == 0:
            return 0
        prefixSum_dict = {0:1}
        prefixSum = 0
        count = 0
        for i in range(num_len):
            prefixSum = prefixSum + nums[i]
            if prefixSum-k in prefixSum_dict:
                count = count + prefixSum_dict[prefixSum-k]
            if prefixSum in prefixSum_dict:
                prefixSum_dict[prefixSum]+=1
            else:
                prefixSum_dict[prefixSum]=1
        return count


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            nums = [int(num) for num in str1.split(",")]
            k = int(str2)
            res = solution.subarraySum(nums, k)
            print(res)
        else:
            break

