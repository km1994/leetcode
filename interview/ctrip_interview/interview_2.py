'''
    求最小客服人数
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

