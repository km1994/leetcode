'''
    0-1背包问题
    
    有一个背包，他的容量为C(Capacity)。现在有n中不同的物品，编号为0…n-1，其中每一件物品的重量为w(i)，价值为v(i)。问可以向这个背包中盛放哪些物品，使得在不超过背包容量的基础上，物品的总价值最大。

'''
class Solution:
    def bag(self, n,c,w,p):
        '''
        :param n int 物品件数
        :param c int 最大承重为c的背包
        :param w list 各个物品的重量
        :param p list 各个物品的价值
        :return
            res list
        '''
        res=[[-1 for j in range(c+1)]for i in range(n+1)]
        #print(res)
        # 第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
        for j in range(c+1):
            res[0][j] = 0

        for i in range(1,n+1):
            for j in range(1,c+1):
                res[i][j]=res[i-1][j]
                #生成了n*c有效矩阵，以下公式w[i-1],p[i-1]代表从第一个元素w[0],p[0]开始取。
                if(j>=w[i-1]) and res[i-1][j-w[i-1]]+p[i-1]>res[i][j]:
                    res[i][j]=res[i-1][j-w[i-1]]+p[i-1]
        return res
        
    def show(self,n,c,w,res):  
        print('最大价值为:',res[n][c])  
        x=[False for i in range(n)]  
        j=c  
        for i in range(1,n+1):  
            if res[i][j]>res[i-1][j]:  
                x[i-1]=True  
                j-=w[i-1]  
        print('选择的物品为:') 
        print(x) 
        for i in range(n):  
            if x[i]:  
                print('第',i,'个,')
    

if __name__ == "__main__":

    solution = Solution()
    print("---------------1----------------")
    n=5  
    c=10  
    w=[2,2,6,5,4]  
    p=[6,3,5,4,6] 
    res = solution.bag(n,c,w,p)  
    print("res:{0}".format(res))
    solution.show(n,c,w,res)

   