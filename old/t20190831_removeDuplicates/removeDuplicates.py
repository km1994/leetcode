#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/31
@url：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
@desc:
    80. 删除排序数组中的重复项 II
    
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    
    示例 1:
        给定 nums = [1,1,1,2,2,3],
        函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
        你不需要考虑数组中超出新长度后面的元素。
    示例 2:
        给定 nums = [0,0,1,1,1,1,2,3,3],
        函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
        你不需要考虑数组中超出新长度后面的元素。
    说明:
        为什么返回数值是整数，但输出的答案是数组呢?
        请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
    你可以想象内部操作如下:

    // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
    int len = removeDuplicates(nums);

    // 在函数里修改输入数组对于调用者是可见的。
    // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }

'''

class Solution:

    def removeDuplicates(self, nums):
        nums_len = len(nums)
        if nums_len < 3:
            return nums_len
        i = 1
        j = 0
        flag = True
        while i < nums_len:
            if nums[i] == nums[j] and flag:
                j = j + 1
                nums[j] = nums[i]
                i = i + 1
                flag = False
            elif nums[i] == nums[j] and  not flag:
                nums[j] = nums[i]
                i = i + 1
            elif nums[i] != nums[j]:
                j = j + 1
                nums[j] = nums[i]
                i = i + 1
                flag = True
        nums = nums[:j+1]
        print(nums)
        return j+1


if __name__ == "__main__":

    print("--------1-------")
    nums = [1,1,1,2,2,3]
    solution = Solution()
    res=solution.removeDuplicates(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = [0,0,1,1,1,1,2,3,3]
    solution = Solution()
    res=solution.removeDuplicates(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums = [1]
    solution = Solution()
    res=solution.removeDuplicates(nums)
    print("res:{0}".format(res))

    print("--------4-------")
    nums = [1,1]
    solution = Solution()
    res=solution.removeDuplicates(nums)
    print("res:{0}".format(res))

    print("--------5-------")
    nums = [0,0,1,1,1,1,2,3,3]
    solution = Solution()
    res=solution.removeDuplicates(nums)
    print("res:{0}".format(res))

    