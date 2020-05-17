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
    def generate(self, rowIndex):

        pre_res = []
        for row_num in range(rowIndex+1):
            
            now_row = [None for _ in range(row_num+1)]
            now_row[0], now_row[-1] = 1, 1

            for j in range(1, len(now_row)-1):
                now_row[j] = pre_res[j-1] + pre_res[j]
            pre_res = now_row
        return pre_res

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

