'''
	t20190226：【每日一问】
	给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
	示例 :给定数组 nums = [-1, 0, 1, 2, -1, -4]，
	满足要求的三元组集合为：
	[ [-1, 0, 1], [-1, -1, 2]]
'''
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
 
def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1

import math
def select_gourp(array,len):
	l_s = 0 * len
	l_e = math.floor(1.0/2*len) -1 
	r_s = math.floor(1.0/2*len)
	r_e = len - 1 
	print(f"l_s:{l_s}")
	print(f"l_e:{l_e}")
	print(f"r_s:{r_s}")
	print(f"r_e:{r_e}")
	l=0
	r=len-1
	while l<r:
		temp = -(array[r] - array[l])
		if (temp > array[l]) and (temp <= array[l_e]):
			for i in range(l-1,l_e+1):
				if array[i] == temp:
					print(f"array[{i}]={array[i]}")

		if (temp >= array[r_s]) and (temp < array[r]):
			for i in range(r_s,r):
				if array[i] == temp:
					print(f"array[{i}]={array[i]}")
		l = l + 1
		r = r - 1

nums = [2, 0, 1, 2, -1, -4]
print(f"nums:{nums}")
quick_sort(nums,0,5)
print(f"nums:{nums}")

select_gourp(nums,6)


