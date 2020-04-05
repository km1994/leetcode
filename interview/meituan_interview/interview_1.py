'''
    题目描述：
    给出一个序列包含n个正整数的序列A，你可以从中删除若干个数，使得剩下的数字中的最大值和最小值之差不超过x，请问最少删除多少个数字。 

    输入
    输入第一行仅包含两个正整数n和x，表示给出的序列的长度和给定的正整数。(1<=n<=1000,1<=x<=10000)

    接下来一行有n个正整数，即这个序列，中间用空格隔开。(1<=a_i<=10000)

    输出
    输出仅包含一个正整数，表示最少删除的数字的数量。


    样例输入
    5 2
    2 1 3 2 5
    样例输出
    1

'''

class Solution:
    def remove_num(self,n,x,nums):
        nums = sorted(nums)
        if nums[n-1]-nums[0] <=x:
            return 0
        best_n = n
        
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[j] - nums[i] > x and best_n > n-j+i:
                    best_n =  n-j+i+1
                    break
        return best_n 

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1!="" and str2!="":
            n,x = str1.split(" ")
            n = int(n)
            x = int(x)
            nums = [int(num) for num in str2.split(" ")]

            res = solution.remove_num(n,x,nums)
            print(res)
        else:
            break

