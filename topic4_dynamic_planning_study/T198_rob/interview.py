'''
    198. 打家劫舍
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

    示例 1:

    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:

    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。

'''
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 动态规划法 采用列表法
    def rob1(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        res = nums[0]
        for i in range(1,nums_len):
            if i == 1:
                nums[i] = nums[i] if nums[i]>nums[i-1] else nums[i-1]
            else:
                temp = nums[i]+nums[i-2]
                nums[i] = temp if temp>nums[i-1] else nums[i-1]
            res = nums[i] if nums[i]>res else res
        return res

    # 动态规划法 保存上一个值
    def rob(self, nums):
        pre = 0
        res = 0
        for num in nums:
            temp = pre+num
            pre = temp if temp>res else res
            pre,res = res,pre
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            num1 = [int(c) for c in str1.split(",")]
            res = solution.rob(num1)
            print(res)
        else:
            break

