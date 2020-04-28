'''
    面试题56 - I. 数组中数字出现的次数

    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

    示例 1：

    输入：nums = [4,1,4,6]
    输出：[1,6] 或 [6,1]
    示例 2：

    输入：nums = [1,2,10,4,1,4,3,3]
    输出：[2,10] 或 [10,2]
     

    限制：

    2 <= nums <= 10000

'''
class Solution:
    def singleNumbers(self, nums):
        res_set = set()
        for num in nums:
            if num not in res_set:
                res_set.add(num)
            else:
                res_set.remove(num)
        return list(res_set)
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.singleNumbers(nums)
            print(res)
        else:
            break

