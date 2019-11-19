#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] > pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


for line in sys.stdin:
    str_list = line.replace("\n","").split(",")
    str_list1 = str_list
    if str_list is '':
        print('')
    else:
        str_len = len(str_list)
        quickSort(str_list,0,str_len-1)
        print(",".join(str_list))

        sorted(str_list1)
        print(str_list1)

        

    