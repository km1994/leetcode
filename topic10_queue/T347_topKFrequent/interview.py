'''
    347. 前 K 个高频元素

    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

    示例 1:

    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]
    示例 2:

    输入: nums = [1], k = 1
    输出: [1]
    说明：

    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

'''
from collections import Counter
class Solution:
    # 方法一：api 法
    def maxSlidingWindow1(self, nums, k):
        return [i[0] for i in Counter(nums).most_common(k)]
        

      
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = [int(num) for num in str1.split(",")]
            k = int(str2)
            res = solution.maxSlidingWindow1(nums, k)
            print(res)
        else:
            break

