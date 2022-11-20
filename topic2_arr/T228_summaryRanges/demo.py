'''
    228. 汇总区间
    给定一个  无重复元素 的 有序 整数数组 nums 。

    返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

    列表中的每个区间范围 [a,b] 应该按如下格式输出：

    "a->b" ，如果 a != b
    "a" ，如果 a == b
     

    示例 1：

    输入：nums = [0,1,2,4,5,7]
    输出：["0->2","4->5","7"]
    解释：区间范围是：
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"
    示例 2：

    输入：nums = [0,2,3,4,6,8,9]
    输出：["0","2->4","6","8->9"]
    解释：区间范围是：
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"

'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        nums_len = len(nums)
        # step 1: 判空
        if not nums_len:
            return res
        # step 2: 遍历 
        i = 0
        while i<nums_len:
            start_idx = i 
            i +=1
            # step 3: 寻找 相邻元素之间的差值大于 1 的 区间
            while i<nums_len and nums[i]==nums[i-1]+1:
                i+=1
            end_idx = i-1 
            # step 4: 区间 入库
            if start_idx<end_idx:
                res.append(f"{nums[start_idx]}->{nums[end_idx]}")
            else:
                res.append(f"{nums[start_idx]}")
        return res
            
    

if __name__ == "__main__":
    
    solution = Solution()
    nums = [0,1,2,4,5,7]
    res = solution.summaryRanges(nums)
    print(res)
    nums = [0,2,3,4,6,8,9]
    res = solution.summaryRanges(nums)
    print(res)

    
  