'''
    977. 有序数组的平方

    给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

    示例 1：

    输入：[-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    示例 2：

    输入：[-7,-3,2,3,11]
    输出：[4,9,9,49,121]

'''
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
            思路：
                1. 定义左右指针从两边向中间遍历：
                    1. 计算平方，将较大的插入 列表res 前部；
                2. 左右指针相遇
        '''
        A_len = len(A)
        if A_len==0:
            return []
        l = 0 
        r = A_len-1
        res = [0] * A_len
        while l<=r:
            l_tmp= A[l]*A[l]
            r_tmp= A[r]*A[r]
            if l_tmp>r_tmp:
                res[A_len-1]=l_tmp
                l = l+1
            else:
                res[A_len-1]=r_tmp
                r= r-1
            A_len = A_len-1
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.sortedSquares(nums)
            print(res)
        else:
            break

