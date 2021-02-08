'''
   229. 求众数 II

   给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

    说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

    示例 1:

    输入: [3,2,3]
    输出: [3]
    示例 2:

    输入: [1,1,1,3,3,2,2,2]
    输出: [1,2]

'''
import math
class Solution:

    # 哈希表
    def majorityElement(self, nums):
        '''
            问题分析：
                
            思路：
                
        '''
        res = []
        nums_len = len(nums)
        countDict = {}
        threshold = math.floor(nums_len/3)
        for num in nums:
            if num not in countDict:
                countDict[num] = 0
            if countDict[num]!= -1:
                print(111)
                countDict[num] +=1
            if countDict[num]>threshold:
                res.append(num)
                countDict[num] = -1
        return res

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            res = solution.majorityElement(nums1)
            print(res)
        else:
            break

