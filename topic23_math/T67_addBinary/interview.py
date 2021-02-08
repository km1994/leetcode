'''
    67. 二进制求和
    
    给你两个二进制字符串，返回它们的和（用二进制表示）。

    输入为 非空 字符串且只包含数字 1 和 0。

     

    示例 1:

    输入: a = "11", b = "1"
    输出: "100"
    示例 2:

    输入: a = "1010", b = "1011"
    输出: "10101"

'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_flag = 0  # 是否进位
        sum_str = ''
        i = len(a)-1
        j = len(b)-1
        while i >=0 and j >=0:
            temp = int(a[i]) + int(b[j]) + carry_flag
            if temp > 1:
                temp = temp%2
                carry_flag = 1
            else:
                carry_flag = 0

            sum_str = str(temp) + sum_str  
            i = i - 1
            j = j - 1
    
        while i >=0:
            temp = int(a[i]) + carry_flag
            if temp > 1:
                temp = temp%2
                carry_flag = 1
            else:
                carry_flag = 0
        
            sum_str = str(temp) + sum_str  
            i = i - 1

        while j >=0:
            temp = int(b[j]) + carry_flag
            if temp > 1:
                temp = temp%2
                carry_flag = 1
            else:
                carry_flag = 0
        
            sum_str = str(temp) + sum_str  
            j = j - 1

        if carry_flag:
            sum_str = '1' + sum_str  
        
        return sum_str

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            res = solution.addBinary(str1,str2)
            print(res)
        else:
            break

