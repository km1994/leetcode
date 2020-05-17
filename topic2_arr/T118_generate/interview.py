'''
    118. 杨辉三角

    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

    示例:

    输入: 5
    输出:
    [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1]
    ]

'''
class Solution:
    def generate(self, numRows):
        res = []
        for row_num in range(numRows):
            
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = res[row_num-1][j-1] + res[row_num-1][j]

            res.append(row)
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = int(str1)
            res = solution.generate(nums)
            print(res)
        else:
            break

