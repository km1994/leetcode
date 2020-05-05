'''
   神奇数字

   题目描述
    在这个特殊的假期里，由于牛牛在家特别无聊，于是他发明了一个小游戏，游戏规则为：将字符串数字中为偶数位的数字进行翻转，将翻转后的结果进行输出。
    示例1
    输入
        "1234"
    输出
        "1432"
    说明
    第2、4位为偶数，所以将其翻转后，得到 1432
    示例2
    输入
        "12346"
    输出
        "16342"
    说明
    第2、4、5位为偶数，所以将其翻转后，得到 16342

'''
class Solution:
    def change(self , number):
        number = list(number)
        num_len = len(number)
        l = 0
        r =num_len -1
        while l < r:
            while l < r and int(number[l])%2 != 0:
                l = l + 1
            while l < r and int(number[r])%2 != 0:
                r = r - 1
            number[l],number[r] = number[r],number[l]
            l = l + 1
            r = r - 1
        return ''.join(number)


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            number = str1
            res = solution.change(number)
            print(res)
        else:
            break

