'''
    491. 递增子序列

    给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

    示例:

    输入: [4, 6, 7, 7]
    输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

'''
class Solution:
    # 动态规划
    def findSubsequences(self, nums):
        '''
            思路：
                1. 定义 一个 集合 pres 来保存 所有 递增子序列
                2. 将 nums[0] 加入集合
                3. 遍历 nums[1:]:
                    3.1 若 num 合并 到 pres 的 子集中，该子集 还是 一个递增子序列，则更新 该子集，并将 num 作为 子集 加入 pres;
                4. 抽取出 所有长度 大于 2 的 pres，即为 结果        
        '''
        if nums==[]:
            return []
        pres = {(nums[0],)}
        print(f"pres:{pres}")
        for num in nums[1:]:
            pres.update({pre+(num,) for pre in pres if pre[-1]<=num})
            pres.add((num,))
        return [list(pre) for pre in pres if len(pre)>1]
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.findSubsequences(nums)
            print(res)
        else:
            break

