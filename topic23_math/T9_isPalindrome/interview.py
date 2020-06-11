'''
    9. 回文数
    
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

    输入: 121
    输出: true
    示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。

'''
class Solution:
    def isPalindrome(self, x) -> bool:
        x=str(x)
        x_len = len(x)
        l = 0
        r = x_len-1
        while l<r:
            if x[l]==x[r]:
                l+=1
                r-=1
            else:
                return False
        return True

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            num = int(str1)

            res = solution.isPalindrome(num)
            print(res)
        else:
            break

