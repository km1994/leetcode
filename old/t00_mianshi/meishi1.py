#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 

def selec_min_index(F_list,F_min):
    for i in range(len(F_list)):
        if F_list[i] == F_min:
            return i

def select_2_min(F_list,F_min):
    F_2_min_index = 0
    for i in range(len(F_list)):
        if F_list[i] > F_list[F_2_min_index]:
            F_2_min_index = i
            break

    for i in range(len(F_list)):
        if F_list[i] < F_list[F_2_min_index] and F_list[i] > F_min:
            F_2_min_index = i
    
    print("F_2_min_index:",F_2_min_index)
    return F_2_min_index

def select_min(F_list):
    F_min = min(F_list)
    print(F_min)
    min_index = selec_min_index(F_list,F_min)

    F_2_min_index = select_2_min(F_list,F_min)
    F_list[F_2_min_index] += F_list[min_index]

    F_list.pop(min_index)

    return F_list


for line in sys.stdin:
    a = line.split()

    a = [int(x) for x in a]
    n = a[0]
    m = a[1]
    F_list = a[2:]
    print(F_list)
    for i in range(m):
        F_list = select_min(F_list)
        print(F_list)

    print("min(F_list):",min(F_list))