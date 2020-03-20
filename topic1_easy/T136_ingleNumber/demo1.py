'''

'''
class Solution:
    # 利用字典方法
    def singleNumber1(self, nums):
        record_dict = {}
        for n in nums:
            if n not in record_dict:
                record_dict[n] = 0
            else:
                record_dict.pop(n)
        return list(record_dict.keys())[0]

    # 位运算
    def singleNumber2(self, nums):
        res = 0
        for n in nums:
            res ^= n
        return res


if __name__ == "__main__":
    
    print(1^3)
    print(5^3)
    print(7^3)
    print(5^7)
    print(9^3)
    print(15^13)

    print(12^10)
    print(2^10)
    print(22^6)

        


  