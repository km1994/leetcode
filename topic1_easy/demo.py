'''
    136. 只出现一次的数字
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

    说明：

    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

    示例 1:

        输入: [2,2,1]
        输出: 1
    示例 2:

        输入: [4,1,2,1,2]
        输出: 4
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
    
    solution = Solution()
    print("--------利用字典方法--------")
    arr1 = [2,2,1]
    res = solution.singleNumber1(arr1)
    print(res)
    arr1 = [4,1,2,1,2]
    res = solution.singleNumber1(arr1)
    print(res)

    print("--------位运算--------")
    arr1 = [2,2,1]
    res = solution.singleNumber2(arr1)
    print(res)
    arr1 = [4,1,2,1,2]
    res = solution.singleNumber2(arr1)
    print(res)





        


  