'''
    268. 缺失数字
    给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

    示例 1:

    输入: [3,0,1]
    输出: 2
    示例 2:

    输入: [9,6,4,2,3,5,7,0,1]
    输出: 8

'''
class Solution:
    def missingNumber(self, nums):
        nums = sorted(nums)
        now_num = 0
        for num in nums:
            if now_num == num:
                now_num = now_num + 1
            else:
                return now_num
        return now_num
    
    def missingNumber1(self, nums):
        temp_set = set()
        for num in nums:
            temp_set.add(num)
        for i in range(0,len(nums)+1):
            if i not in temp_set:
                return i

    def missingNumber2(self, nums):
        temp_num = len(nums)
        for i,num in enumerate(nums):
            temp_num = temp_num^i^num
        return temp_num

if __name__ == "__main__":
    
    solution = Solution()
    print("-----------1-----------")
    nums = [3,0,1]
    res = solution.missingNumber2(nums)
    print(res)

    print("-----------2-----------")
    nums = [9,6,4,2,3,5,7,0,1]
    res = solution.missingNumber2(nums)
    print(res)



    


    







        


  