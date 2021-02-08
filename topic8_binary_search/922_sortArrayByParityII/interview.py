'''
   922. 按奇偶排序数组 II
   给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

    对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

    你可以返回任何满足上述条件的数组作为答案。

'''
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A_len = len(A)
        l = 0
        r = A_len-1
        # step 1 :奇偶分割
        while l<r  and l<A_len and r>0:
            while l<r and A[l]%2==0:
                l = l+1
            while l<r and A[r]%2==1:
                r = r-1
            A[l],A[r] = A[r],A[l]
            l = l+1
            r = r-1
        # step 2 : 隔位交换
        l = 1
        r = A_len-2
        while l<r and l<A_len and r>0:
            A[l],A[r] = A[r],A[l]
            l = l+2
            r = r-2
        return A

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.sortArrayByParityII(nums)
            print(res)
        else:
            break

