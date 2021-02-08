'''
   350. 两个数组的交集 II

   给定两个数组，编写一个函数来计算它们的交集。

    示例 1：

    输入：nums1 = [1,2,2,1], nums2 = [2,2]
    输出：[2,2]
    示例 2:

    输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出：[4,9]

'''
class Solution:

    # 哈希表
    def intersect(self, nums1, nums2):
        '''
            问题分析：
                这道题 与 两个数组的交集 I 的 区别 在于 ，这道题需要考虑重复的值，也就是 不能够直接用词典处理
            思路：
                1. 可以采用一个 词典计算器 来记录 num1 中 每个值出现的次数；
                2. 对 nums2 进行遍历：
                    当 num1_dict[n2] 存在而且 大于零时，将 n2 加入到 结果中，并对 num1_dict[n2] -= 1
        '''
        num1_dict = {}
        res = []
        for n in nums1:
            if n in num1_dict:
                num1_dict[n] += 1
            else:
                num1_dict[n] = 1
        for n in nums2:
            if n in num1_dict and num1_dict[n] >0:
                res.append(n)
                num1_dict[n] -= 1
        return res


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            nums1 = [int(num) for num in str1.split(",")]
            nums2 = [int(num) for num in str2.split(",")]
            res = solution.intersect(nums1, nums2)
            print(res)
        else:
            break

