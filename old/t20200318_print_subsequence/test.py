input_str = 'abc'
str_list =  []
temp_str = ''
for i in range(0,len(input_str)):
	temp_str = input_str[i]
	str_list.append(temp_str)
	for j in range(i+1,len(input_str)):
		temp_str = temp_str + input_str[j]
		str_list.append(temp_str)


print(str_list)