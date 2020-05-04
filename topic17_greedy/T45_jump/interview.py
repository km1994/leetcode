'''
    45. 跳跃游戏 II

    给定一个非负整数数组，你最初位于数组的第一个位置。

    数组中的每个元素代表你在该位置可以跳跃的最大长度。

    你的目标是使用最少的跳跃次数到达数组的最后一个位置。

    示例:

    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

'''
class Solution:
    # 动规 超时
    def jump1(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        dp = [nums_len+1]*nums_len
        dp[0] = 0
        for i in range(1,nums_len):
            for j in range(0,i):
                if nums[j] + j >= i:
                    dp[i] = dp[i] if dp[i]<dp[j]+1 else dp[j]+1
            
        return dp[-1]
            
    # 动态规划
    def jump2(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 1
        jump_min_list = [0] * nums_len  #
        jump_flag_list = [True] * nums_len  #

        jump_min_list[0] = 0 # 第一阶只有一种可能

        for i in range(1,nums_len):
            jump_min = nums_len
            for step in range(i,0,-1):
                if jump_flag_list[i-step]:
                    if step <= nums[i-step]:
                        if jump_min > jump_min_list[i-step]+1:
                            jump_min = jump_min_list[i-step]+1
                    else:
                        jump_flag_list[i-step]=False
            jump_min_list[i] = jump_min
        
        return jump_min_list[-1]

    # 解法三 ：顺藤摸瓜 贪心算法
    def jump3(self, nums):
        end = 0
        max_position = 0
        steps = 0
        nums_len = len(nums)
        for i in range(0,nums_len-1):
            max_position = max(max_position,nums[i]+i)
            if i == end:
                end = max_position 
                steps = steps + 1

        return steps

    # 解法四 顺瓜摸藤 贪心算法
    def jump4(self, nums):
        position = len(nums) - 1
        steps = 0
        while position != 0:
            for i in range(0,position):
                if nums[i] >= position -i:
                    position = i
                    steps = steps + 1
                    break
        
        return steps
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.jump4(nums)
            print(res)
        else:
            break

