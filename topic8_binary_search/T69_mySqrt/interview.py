''' 69. x 的平方根

    实现 int sqrt(int x) 函数。

    计算并返回 x 的平方根，其中 x 是非负整数。

    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

    示例 1:

    输入: 4
    输出: 2
    示例 2:

    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842..., 
         由于返回类型是整数，小数部分将被舍去。

'''
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    '''
        方法一 二分法
    '''
    def mySqrt(self, x):
        '''
            二分法
            :param x: int
            :return:
                ans  int
        '''
        if x==1:
            return x
        l = 0
        r = x//2
        # res = -1
        while l<=r:
            mid = l + (r-l)//2
            if mid*mid <=x:
                # res = mid
                l = mid+1   # 结果在右半期间内
            else:
                r = mid - 1 # 结果在左半期间内
        return l-1

if __name__ == "__main__":

    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            num = int(str1)
            res = solution.mySqrt(num)
            print(res)
        else:
            break

   