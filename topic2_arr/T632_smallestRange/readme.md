# 632. 最小区间

## 题目描述

    你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

    我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

## 示例:
```
   示例 1:
        输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
        输出: [20,24]
    解释: 
        列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
        列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
        列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
```

## 思路介绍

### 方法一：k 指针法

#### 题目解析



#### 思路

1. 定义列表 index_list 用于 存储 指向每个 列表当前位置 的 指针；
2. 定义列表 val_list 用于 存储 每个 指针 所 指向 的当前值；
3. 初始化，也就是 指针都 指向 每个列表 第一个 位置
4. 计算 val_list 的 最大、最小值，因为该题目标是要 确定最小区间，而该区间的大小与这两个值相关；
5. 每个指针 不断 往后移动，直到某个 指针 当前值最小，而且已经指向对于 列表的最后一个元素，即不能再往后以后：
   1. 获取 当前 val_list 的 最大、最小值；
   2. 比较 当前区间 与 当前最小区间 的大小，若小于，则替换；
   3. 获得 val_list 数组最小值 所 对于 的 位置，也就是 最小值 所属于的 列表；
   4. 判断 最小值的指针 是否 到达 所属列表 的尾部：
      1. 若不是，继续下移，并将 指针 所指值 加入 val_list；
      2. 若是，表示找到最小区间，跳出循环

#### 代码

```python
    class Solution:
    def smallestRange(self, nums):
        nums_len = len(nums)
        index_list = [0]*nums_len   # 用于 存储 指向每个 列表当前位置 的 指针
        val_list = [0]*nums_len     # 用于 存储 每个 指针 所 指向 的当前值
        # 初始化，也就是 指针都 指向 每个列表 第一个 位置
        for i in range(nums_len):
            val_list[i] = nums[i][index_list[i]]
        # 计算 val_list 的 最大、最小值，因为该题目标是要 确定最小区间，而该区间的大小与这两个值相关
        max_val,min_val = max(val_list),min(val_list)

        # 每个指针 不断 往后移动，直到某个 指针 当前值最小，而且已经指向对于 列表的最后一个元素，即不能再往后以后
        while True:
            # 获取 当前 val_list 的 最大、最小值
            curr_max_val,curr_min_val = max(val_list),min(val_list)
            # 比较 当前区间 与 当前最小区间 的大小，若小于，则替换
            if curr_max_val-curr_min_val<max_val-min_val:
                max_val=curr_max_val
                min_val=curr_min_val
            # 获得 val_list 数组最小值 所 对于 的 位置，也就是 最小值 所属于的 列表
            index=val_list.index(curr_min_val)
            # 判断 最小值的指针 是否 到达 所属列表 的尾部
            # 若不是，继续下移，并将 指针 所指值 加入 val_list
            if index_list[index]<len(nums[index])-1:
                index_list[index]+=1
                val_list[index]=nums[index][index_list[index]]
            # 若是，表示找到最小区间，跳出循环
            else:
                break
        return [min_val,max_val]

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        str3 = input()
        if str1 != "" and str2!="" and str3!="":
            nums1 = [int(s) for s in str1.split(",")]
            nums2 = [int(s) for s in str2.split(",")]
            nums3 = [int(s) for s in str3.split(",")]
            res = solution.smallestRange([nums1,nums2,nums3])
            print(res)
        else:
            break
```

#### 复杂度计算

> 时间复杂度：O(n*m)
>  
> 空间复杂度：O(2k)

