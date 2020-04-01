
class Solution:
    def count_str(self,a_len,b_len,s,k_list):
        count = 0
        temp_count = 0
        for i in range(0,a_len):
            if s[i] in k_list:
                temp_count = 1 if temp_count == 0 else 2
                count = count + temp_count 
            else:
                temp_count = 0
        return count


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        s = input()
        k_list = input().split(" ")
        
        if str1!="":
            a_len,b_len = str1.split(" ")
            print(a_len,b_len)
            print(s)
            print(k_list)
            res = solution.count_str(int(a_len),int(b_len),s,k_list)
            print(res)
        else:
            break

