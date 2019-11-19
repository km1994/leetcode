'''
    202. 快乐数
'''
import math
class Solution:
    # 循环法，阙值出现问题
    def isHappy1(self, n):
        count = 0
        level =1000
        while count < level:
            curr_num = math.pow(n%10,2)
            while int(n/10) != 0:
                curr_num = curr_num +math.pow(n/10,2)
                n = int(n/10)
            if curr_num == 1:
                return True
            count = count + 1
        return False

    # 快慢指针
    def isHappy(self, n):
        slow = n
        fast = n
        slow = self.bitSquareSum(slow)
        fast = self.bitSquareSum(fast)
        fast = self.bitSquareSum(fast)
        while slow != fast:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)

        return slow == 1

    def bitSquareSum(self,n):
        sum = 0
        while n > 0:
            bit = n%10
            sum = sum + bit* bit
            n = int(n/10)
        return sum
    


if __name__ == "__main__":

    solution = Solution()
    print("---------------1----------------")
    num  = 19
    res = solution.isHappy(num)
    print("res:{0}".format(res))



        


  