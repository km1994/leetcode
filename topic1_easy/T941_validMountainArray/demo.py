'''
    941. 有效的山脉数组

    给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

    让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

    A.length >= 3
    在 0 < i < A.length - 1 条件下，存在 i 使得：
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]

    示例 1：
        输入：[2,1]
        输出：false
    示例 2：
        输入：[3,5,5]
        输出：false
    示例 3：
        输入：[0,3,2,1]
        输出：true
'''
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        A_len= len(A)
        # 要构建 山脉，那至少需要3个元素
        if A_len<3:
            return False

        p = 0
        # 上坡，越走越高
        while A[p]<A[p+1]:
            p = p+1
            # 当峰巅为尽头时，表示 非山脉
            if p+1 == A_len:
                return False
        # 下坡，越走越矮
        while p+1<A_len and A[p]>A[p+1]:
            # 当峰巅为开始时，表示 非山脉
            if p==0:
                return False
            p = p+1
        # 是否 走完
        return p+1==A_len

if __name__ == "__main__":
    
    solution = Solution()
    A = [0,3,2,1]
    res = solution.validMountainArray(A)
    print(res)






        


  