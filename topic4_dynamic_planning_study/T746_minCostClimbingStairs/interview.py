'''
    746. 使用最小花费爬楼梯

    数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

    每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

    您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

    示例 1:

    输入: cost = [10, 15, 20]
    输出: 15
    解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
     示例 2:

    输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    输出: 6
    解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            记忆型 O(1) 动态规划 （斐波那契数列 衍生题）
            解析：
                该题作为 斐波那契数列衍生题，核心 只要记录 离当前最近的前两个状态值即可；
            思路：
                1. 第一种情况：cost 长度小于等于2，此时 取 min 即可；
                2. 第二种情况：cost 长度大于2：
                    1. 定义 两个变量p,q 存储 离当前最近的前两个状态值；
                    2. 从 3->num_len 遍历：
                        状态方程：p,q = q,min(p+cost[i],q+cost[i])
                3. 最后 取 p,q 最小值者即可
        '''
        cost_len = len(cost)
        if cost_len == 1 or cost_len == 2:
            return min(cost)
        p = cost[0]
        q = cost[1]
        for i in range(2,cost_len):
            p,q = q,min(p+cost[i],q+cost[i])
        return min(p,q)

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.minCostClimbingStairs(nums)
            print(res)
        else:
            break

