'''
    219. 存在重复元素 II
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

    示例 1:

    输入: nums = [1,2,3,1], k = 3
    输出: true
    示例 2:

    输入: nums = [1,0,1,1], k = 1
    输出: true
    示例 3:

    输入: nums = [1,2,3,1,2,3], k = 2
    输出: false

'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        方法：滑动窗口
        思路：
            定义一个 存储集（大小 小于等于 k）
            遍历数组：
                如果 nums[i] 在 sets 中，return True
                否则 将 nums[i] 插入 sets 
                当 sets 大小 超过 k 时，将 nums[i-k] 释放
        """
        # 判空
        nums_len = len(nums)
        if nums_len<k:
            return False 

        sets = set()
        for i in range(nums_len):
            if nums[i] in sets:
                return True 
            sets.add(nums[i])
            if len(sets)>k:
                sets.remove(nums[i-k])
        return False
        
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            arr = [int(a) for a in str1.split(",")]
            k = int(str2)

            res = solution.containsNearbyDuplicate(arr, k)
            print(res)
        else:
            break

