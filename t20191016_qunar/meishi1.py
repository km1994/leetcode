#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 


count = 0
n = 0
arr_input = []
arr_output = []
arr_sum = 0
for line in sys.stdin:
    if count == 0:
        n = int(line.replace('\n',''))
        if n == 0:
            print(arr_sum)
        count = count + 1
    elif count == 1:
        arr_input = [int(a) for a in line.replace('\n','').split(" ")]
        count = 0
        
        if n == len(arr_input):
            type = True
            for i in range(0,n-1):
                if type:
                    min1 = min(arr_input)
                    arr_input.remove(min1)
                    min2 = min(arr_input)
                    arr_input.remove(min2)

                    arr_output.append(min1)
                    arr_output.append(min2)

                    arr_sum = arr_sum + max(min1,min2)
                else:
                    max1 = max(arr_input)
                    arr_input.remove(max1)
                    max2 = max(arr_input)
                    arr_input.remove(max2)

                    arr_output.append(max1)
                    arr_output.append(max2)

                    arr_sum = arr_sum + max(max1,max2)

                if len(arr_input) > 0:
                    min1 = min(arr_output)
                    arr_output.remove(min1)
                    arr_input.append(min1)
                    arr_sum = arr_sum + min1
                
                type = not type

                print("-"*10)
                print(arr_input)
                print(arr_output)
                print("arr_sum:",arr_sum)

        print(arr_sum)












    

    

        

    