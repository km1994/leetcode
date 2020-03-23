'''
    斐波那契数列
'''
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    '''
        方法一 递归法
    '''
    # 功能： 递归法
    def fib1(self, n):
        '''
        递归法
        :param n: int
        :return:
            res：int   fib1(n)
        '''
        if n == 1 or n == 2:
            return 1
        return self.fib1(n-1) + self.fib1(n-2)

    '''
        方法二 带备忘录的递归解法
    '''
    # 功能： 带备忘录的递归解法
    def fib2(self, n):
        '''
        带备忘录的递归解法
        :param n: int
        :return:
            self.helper(meno,n)：int   
        '''
        if n<0:
            return 0
        meno = [0] * (n+1)
        meno[1] = 1
        meno[2] = 1
        return self.helper(meno,n)
    
    def helper(self,meno,n):
        if n > 0 and meno[n] == 0:
            meno[n] = self.helper(meno,n-1) + self.helper(meno,n-2)
        return meno[n]
        
    '''
        方法三 动态规划
    '''
    # 功能： 动态规划
    def fib3(self, n):
        '''
        动态规划
        :param n: int
        :return:
            res：int   meno[n]
        '''
        if n<0:
            return 0
        meno = [0] * (n+1)
        meno[1] = 1
        meno[2] = 1
        for i in range(3,n+1):
            meno[i] = meno[i-1]+meno[i-2]
        return meno[n]

    '''
        方法四 动态规划优化
    '''
    # 功能： 动态规划
    def fib4(self, n):
        '''
        动态规划优化
        :param n: int
        :return:
            res：int   sum
        '''
        if n<0:
            return 0
        pre = 1
        next = 1
        sum = 1
        for i in range(3,n+1):
            sum = pre + next
            pre = next
            next = sum
        return sum


if __name__ == "__main__":

    solution = Solution()
    print("---------------1----------------")
    res = solution.fib1(3)
    print("res:{0}".format(res))

    print("---------------2----------------")
    res = solution.fib2(3)
    print("res:{0}".format(res))

    print("---------------3----------------")
    res = solution.fib3(3)
    print("res:{0}".format(res))

    print("---------------4----------------")
    res = solution.fib4(3)
    print("res:{0}".format(res))


        


  