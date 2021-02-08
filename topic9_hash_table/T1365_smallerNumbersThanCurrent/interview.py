'''
   1365. 有多少小于当前数字的数字

   给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

    换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

    以数组形式返回答案。

    示例 1：

    输入：nums = [8,1,2,2,3]
    输出：[4,0,1,1,3]
    解释： 
    对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
    对于 nums[1]=1 不存在比它小的数字。
    对于 nums[2]=2 存在一个比它小的数字：（1）。 
    对于 nums[3]=2 存在一个比它小的数字：（1）。 
    对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
    示例 2：

    输入：nums = [6,5,4,8]
    输出：[2,1,0,3]
    示例 3：

    输入：nums = [7,7,7,7]
    输出：[0,0,0,0]

'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 判空
        nums_len = len(nums)
        if nums_len==0:
            return []
        # 排序
        nums1 = sorted(nums)
        # 计数
        count_dict = {}
        for num in nums1:
            if num not in count_dict:
                count_dict[num]=0
            count_dict[num]+=1
        # 统计 每个 位置 比他小的数的数量
        tmp = 0
        less_dict = {}
        for key,val in count_dict.items():
            if key not in less_dict:
                less_dict[key]=0
            less_dict[key] = tmp
            tmp = tmp + val
        # 对号入座
        res = []
        for num in nums:
            res.append(less_dict[num])
        return res

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            res = solution.smallerNumbersThanCurrent(nums1)
            print(res)
        else:
            break

