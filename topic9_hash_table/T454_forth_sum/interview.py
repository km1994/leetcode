'''
    454. 四数相加 II

    给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

    为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

    例如:

    输入:
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]

    输出:
        2

    解释:
        两个元组如下:
            1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
            2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

'''
class Solution:
    def fourSumCount1(self, A, B, C, D):
        res = 0
        len1 = len(A)
        if len1 == 0:
            return 0
        temp_dict = {}
        for i in range(len1):
            for j in range(len1):
                temp = -(A[i] + B[j])
                if temp not in temp_dict:
                    temp_dict[temp] = []
                temp_dict[temp].append([i,j])
        
        for i in range(len1):
            for j in range(len1):
                temp = C[i] + D[j]
                if temp in temp_dict:
                    res = res + len(temp_dict[temp])
        return res

    def fourSumCount(self, A, B, C, D):
        res = 0
        temp_dict = {}
        for a in A:
            for b in B:
                temp = -(a + b)
                if temp not in temp_dict:
                    temp_dict[temp] = 0
                temp_dict[temp] = temp_dict[temp] + 1
        
        for c in C:
            for d in D:
                temp = c + d
                if temp in temp_dict:
                    res = res + temp_dict[temp]
        return res
        
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        str4 = input()
        if str1 != "" and str2 != "" and str3 != "" and str4 != "":
            nums1 = [int(num) for num in str1.split(",")]
            nums2 = [int(num) for num in str2.split(",")]
            nums3 = [int(num) for num in str3.split(",")]
            nums4 = [int(num) for num in str4.split(",")]
            res = solution.fourSumCount(nums1, nums2, nums3, nums4)
            print(res)
        else:
            break

