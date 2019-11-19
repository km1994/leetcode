#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 

def fun(x):
    v = 1
    for i in range(1,x+1):
        v = v * i
    return v

def zuhe(n):
    zuhe_list = []

    for i in range(n+1):
        zuhe_list.append(str(int((fun(n))/(fun(i)*fun(n-i)))))
    
    return zuhe_list

for line in sys.stdin:
    n = int(line)

    zuhe_list = zuhe(n)
    print(" ".join(zuhe_list))
    

        

    