'''
    53. 最大子序和

    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            记忆型 O(1) 动态规划 （斐波那契数列 衍生题）
            解析：
                该题作为 斐波那契数列衍生题，核心 只要记录 离当前最近的前两个状态值即可；
            思路：
                1. 第一种情况：nums 长度等于0，此时 取 0 即可；
                2. 第二种情况：nums 长度大于0：
                    1. 定义 两个变量p,q 存储 离当前最近的前两个状态值；
                    2. 从 1->num_len 遍历：
                        状态方程：
                            p,q = q,max(q+nums[i],nums[i])
                            max_sum = max(max_sum,q)
                3. 最后 max_sum
        '''
        nums_len = len(nums)
        if nums_len==0:
            return 0
        max_sum = nums[0]
        p = nums[0]
        q = nums[0]
        for i in range(1,nums_len):
            p,q = q,max(q+nums[i],nums[i])
            max_sum = max(max_sum,q)
        return max_sum

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.maxSubArray1(nums)
            print(res)
        else:
            break

