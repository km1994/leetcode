'''
    201. 数字范围按位与
    
    给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

    示例 1: 

    输入: [5,7]
    输出: 4
    示例 2:

    输入: [0,1]
    输出: 0


'''
class Solution:
    # 方法一：循环按位与 超时
    def rangeBitwiseAnd1(self, m, n):
        res = n
        for i in range(m,n):
            res = res&i
        return res

    # 方法二：位移
    def rangeBitwiseAnd(self, m, n):
        num = 0
        while m<n:
            m >>=1
            n >>=1
            num+=1
        return m<<num
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            res = solution.rangeBitwiseAnd(int(str1),int(str2))
            print(res)
        else:
            break

