#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/26
@url：
@desc:
    有一个淘宝商户，在某城市有n个仓库，每个仓库的储货量不同，
    现在要通过货物运输，将每次仓库的储货量变成一致的，
    n个仓库之间的运输线路围城一个圈，即1->2->3->4->…->n->1->…，
    货物只能通过连接的仓库运输，设计最小的运送成本（运货量*路程）达到淘宝商户的要求，
    并写出代码。

'''

class Solution:
    # 递归法
    def goodsAverage(self, nums):
        aver = self.average(nums)
        print("aver:{0}".format(aver))
        all_full = False
        consumption = 0
        while not all_full:
            difference = 0
            for num in nums:
                all_full = True
                if num > aver:
                    difference = difference + (num - aver)
                else:
                    if aver - num < difference:
                        last = aver - num
                        num = num + last
                        difference = difference - last
                    else:
                        num = num + difference
                        difference = 0
                        all_full = False
                consumption = consumption + difference
            return consumption
            
    def average(self,nums):
        goods_all = 0
        for num in nums:
            goods_all = goods_all + num

        return goods_all/len(nums)
        
        
if __name__ == "__main__":

    print("--------1-------")
    nums = [1,3,4]
    solution = Solution()
    res=solution.goodsAverage(nums)
    print("res:{0}".format(res))

    # print("--------2-------")
    # nums = []
    # solution = Solution()
    # res=solution.subsets(nums)
    # print("res:{0}".format(res))

    