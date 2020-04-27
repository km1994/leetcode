'''
    46. 全排列
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。

    示例:

    输入: [1,2,3]
    输出:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]

'''
import copy
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def permute(self, nums):
        res =[]
        nums_len = len(nums)
        if nums_len == 0:
            return res

        def backtrack(nums,path,res,nums_len):
            if nums_len == 0:
                res.append(path[:])
                return 
 
            for i in range(nums_len):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]],res,nums_len-1)
            
        backtrack(nums,[],res,nums_len)

        return res

    
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(c) for c in str1.split(",")]
            print(f"nums:{nums}")

            res = solution.permute(nums)
            print(res)
        else:
            break

