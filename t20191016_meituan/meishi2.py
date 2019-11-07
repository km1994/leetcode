#coding=utf-8
# 【校招笔试题】字符串排序_美团
# 参考：https://blog.csdn.net/weixin_40583722/article/details/100022733
string = "waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian"
strs = string.split(",")
def compare(s1, s2):
    if not s1:
        return True
    if not s2:
        return False
    for i in range(min(len(s1), len(s2))):
        if s1[i] > s2[i]:
            return True
        elif s1[i] < s2[i]:
            return False
    return True if len(s1) < len(s2) else False

def sort(strs):
    for i in range(len((strs))):
        for j in range(i+1, len(strs)):
            if compare(strs[j], strs[i]):
                strs[i], strs[j] = strs[j], strs[i]
    return strs

strs1 = strs
print("----1-----")
strs1 = sort(strs1)
print(strs1)

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low,high):
        if compare(arr[j], pivot):
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

strs2 = strs
print("----2-----")
quickSort(strs2,0,len(strs2)-1)
print(strs2)

