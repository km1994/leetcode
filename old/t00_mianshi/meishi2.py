#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 

for line in sys.stdin:
    a = line.split()

    a = [int(x) for x in a]
    
    start = a[0]
    end = a[1]
    index = a[-1]

    if index >= 0 and index <=9:
        index = str(index)
    else:
        print(0)

    if start >= end:
        print(0)

    print("start:",start)
    print("end:",end)
    print("index:",index)

    num_str = ''
    for i in range(start+1,end+1):
        num_str += str(i)
    
    print("num_str:",num_str)
    count = 0
    for s in num_str:
        if s == index:
            count = count + 1
    print("count:",count)
