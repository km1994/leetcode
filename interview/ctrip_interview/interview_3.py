'''
    携程海洋馆的海豚小宝宝

    题目描述：
携程海洋馆中有 n 只萌萌的小海豚，初始均为 0 岁，每只小海豚的寿命是 m 岁，

且这些小海豚会在 birthYear[i] 这些年份生产出一位宝宝海豚（1 <= birthYear[i] <= m），每位宝宝海豚刚出生为 0 岁。

问 x 年时，携程海洋馆有多少只小海豚？

输入
n（初始海豚数）

m（海豚寿命）

海豚生宝宝的年份数量(假设为p)

海豚生宝宝的年份1

...

海豚生宝宝的年份p

x（几年后）

输出
x年后，共有多少只小海豚


样例输入
5
5
2
2
4
5
样例输出
20

''' 

class Solution:
    def count_str(self,num,n_list):
        tele_list = []
        for i in range(num):
            if len(tele_list) == 0:
                tele_list.append([int(n_list[i][1]),int(n_list[i][0])])
            else:
                status = 0
                for j in range(len(tele_list)):
                    if int(n_list[i][0]) >= int(tele_list[j][0]):
                        tele_list[j][0] = int(n_list[i][1])
                        tele_list[j][1] = int(n_list[i][0])
                        status = 1
                        break
                if status == 0:
                    tele_list.append([int(n_list[i][1]),int(n_list[i][0])])
        return len(tele_list)

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        num = input()
        error = 0
        if num.isdigit():
            num = int(num)
            n_list = []
            for i in range(num):
                temp = input()
                if temp!='' and len(temp.split(','))==2:
                    n_list.append(temp.split(','))
                else:
                    error = 1
                    break
            res = solution.count_str(num,n_list)
            print(res)
            if error == 1:
                break
        else:
            break

