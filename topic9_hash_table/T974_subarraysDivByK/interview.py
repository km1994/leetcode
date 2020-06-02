'''
  974. 和可被 K 整除的子数组


   给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

    示例：

    输入：A = [4,5,0,-2,-3,1], K = 5
    输出：7
    解释：
    有 7 个子数组满足其元素之和可被 K = 5 整除：
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
     

    提示：

    1 <= A.length <= 30000
    -10000 <= A[i] <= 10000
    2 <= K <= 10000

'''
class Solution:

    # 字典法
    def subarraySum(self, nums, k):
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2!="":
            nums = [int(num) for num in str1.split(",")]
            k = int(str2)
            res = solution.subarraySum(nums, k)
            print(res)
        else:
            break

