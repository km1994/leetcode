'''
    50. Pow(x, n)
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。

    示例 1:

    输入: 2.00000, 10
    输出: 1024.00000
    示例 2:

    输入: 2.10000, 3
    输出: 9.26100
    示例 3:

    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25

'''
class Solution:
     def myPow(self, x, n):
        if not n:   # x 的 0 次方
            return 1

        if n < 0: # 如果 n 小于 0 ，这个时候采用的方法是，计算 x^n 的值，然后在取倒数
            return 1/self.myPow(x,-n)
        if n % 2 == 1:  # 如果 n 为奇数，需要 换成 x 的 奇数幂 除以 x
            return x * self.myPow(x,n-1)
        # 若 n 为 偶数，那么只需要 计算 （x*x）^ (n/2)
        return self.myPow(x*x,n/2)


if __name__ == "__main__":
    
    solution = Solution()
    print("--------利用字典方法--------")
    x = 2
    n = 10
    res = solution.myPow(x, n)
    print(res)


  

        


  