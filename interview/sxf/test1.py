#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 
for line in sys.stdin:
    a = line.split()
    #print(int(a[0]) + int(a[1]))
    N = int(a[0])
    M = int(a[1])
    nums_list = list(range(1,M))
    print(nums_list)
    num = 1
    no = 0
    temp = 10
    while num <=1000 or len(nums_list)>1:
        if int(num/M) == 0 or num%temp == M:
            

    