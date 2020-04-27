'''
    牛妹的蛋糕
    题目描述
        众所周知，牛妹非常喜欢吃蛋糕。
        第一天牛妹吃掉蛋糕总数三分之一（向下取整）多一个，第二天又将剩下的蛋糕吃掉三分之一（向下取整）多一个，以后每天吃掉前一天剩下的三分之一（向下取整）多一个，到第n天准备吃的时候只剩下一个蛋糕。
        牛妹想知道第一天开始吃的时候蛋糕一共有多少呢？

    示例1
        输入
            2
        输出
            3
    示例2
        输入
            4
        输出
            10

'''
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 动态规划法
    def cakeNumber(self , n ):
        res = 1
        for _ in range(n-1,0,-1):
            res = (res+1)*3//2
        return res
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            num1 = int(str1)
            res = solution.cakeNumber(num1)
            print(res)
        else:
            break

