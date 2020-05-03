'''
   202. 快乐数

   编写一个算法来判断一个数 n 是不是快乐数。

    「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

    如果 n 是快乐数就返回 True ；不是，则返回 False 。

    示例：

    输入：19
    输出：true
    解释：
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

'''
class Solution:

    # 迭代
    def isHappy(self, n: int) -> bool:
        for _ in range(10):
            n=self.bitSquareSum(n)
            if n==1:
                return True
        return False


    # 快慢指针法
    def isHappy1(self, n: int) -> bool:
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
            n = n//10
        return sum


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums =int(str1)
            res = solution.isHappy(nums)
            print(res)
        else:
            break

