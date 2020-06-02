'''
    1343. 大小为 K 且平均值大于等于阈值的子数组数目
    
    给你一个整数数组 arr 和两个整数 k 和 threshold 。

    请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

    示例 1：

    输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    输出：3
    解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
    示例 2：

    输入：arr = [1,1,1,1,1], k = 1, threshold = 0
    输出：5
    示例 3：

    输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
    输出：6
    解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
    示例 4：

    输入：arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
    输出：1
    示例 5：

    输入：arr = [4,4,4,4], k = 4, threshold = 1
    输出：1
     

    提示：

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 10^4
    1 <= k <= arr.length
    0 <= threshold <= 10^4

'''
import math
class Solution:
    # 滑动窗口 （超时）
    def numOfSubarrays1(self, arr, k, threshold):
        res = 0
        arr_len = len(arr)
        if arr_len<k:
            return res
        for i in range(arr_len-k+1):
            if sum(arr[i:i+k])/k >= threshold:
                res += 1
        return res
    # 
    def numOfSubarrays(self, arr, k, threshold):
        
        arr_len = 0
        if arr_len<k:
            return 0
        i = 0
        temp_sum = 0
        while i<k:
            temp_sum += arr[i]
            i += 1
        res = 0 if temp_sum//k<threshold else 1
        i = k
        while i < arr_len:
            temp_sum = temp_sum - arr[i-k] + arr[i]
            if temp_sum//k>=threshold:
                res = res+1
            i +=1
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        if str1 != "" and str2 != "" and str3 != "":
            arr = [int(a) for a in str1.split(",")]
            k = int(str2)
            threshold = int(str3)

            res = solution.numOfSubarrays(arr, k, threshold)
            print(res)
        else:
            break

