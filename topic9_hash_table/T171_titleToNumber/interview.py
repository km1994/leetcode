'''
    171. Excel表列序号

    给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    示例 1:

    输入: "A"
    输出: 1
    示例 2:

    输入: "AB"
    输出: 28
    示例 3:

    输入: "ZY"
    输出: 701


'''
class Solution:
    def __init__(self):
        self.letter2num_dict = {}
        for num in range(65,65+26):
            self.letter2num_dict[chr(num)] = num


    def titleToNumber1(self, s):
        res = 0
        for c in s:
            num = self.letter2num_dict[c] - self.letter2num_dict['A'] + 1
            res = res * 26 + num
        return res

    def titleToNumber(self, s):
        res = 0
        for c in s:
            num = ord(c) -  64 
            res = res * 26 + num
        return res
  
if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            res = solution.titleToNumber(str1)
            print(res)
        else:
            break

