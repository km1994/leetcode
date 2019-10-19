#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 

def zoufa(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return zoufa(n-1) + zoufa(n-2)



for line in sys.stdin:
    a = int(line)
    print(zoufa(a))




    