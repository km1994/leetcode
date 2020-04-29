'''
    1095. 山脉数组中查找目标值

    （这是一个 交互式问题 ）

    给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

    如果不存在这样的下标 index，就请返回 -1。

    何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

    首先，A.length >= 3

    其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]
     

    你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

    MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
    MountainArray.length() - 会返回该数组的长度
     
    注意：

    对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

    为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

    示例 1：

    输入：array = [1,2,3,4,5,3,1], target = 3
    输出：2
    解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
    示例 2：

    输入：array = [0,1,2,4,2,1], target = 3
    输出：-1
    解释：3 在数组中没有出现，返回 -1。
     
    提示：

    3 <= mountain_arr.length() <= 10000
    0 <= target <= 10^9
    0 <= mountain_arr.get(index) <= 10^9

'''
class MountainArr:
    def __init__(self,nums):
        self.nums = nums
        self.nums_len = len(nums)

    def get(self,index):
        return nums[index]

    def length(self):
        return self.nums_len


class Solution:

    def findInMountainArray(self, target, mountain_arr):
        nums_len = mountain_arr.length()
        '''
            step 1 需要 坡顶
        '''
        l = 0 
        r = nums_len - 1
        mid = l + (r-l)//2
        while l <= r:
            # 若 mid 前一个元素小于 mid 元素，说明 mid 暂时处于递增区间
            if mountain_arr.get(mid-1) < mountain_arr.get(mid):
                # 若 mid 后一个元素大于 mid 元素，确定 mid 一定处于递增区间
                if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    l = mid + 1
                else:
                    # 否则 mid 元素为峰值元素
                    break
            else:
                # 如果 mid 的前一个元素大于 mid 元素，则 mid 一定处于单调递减区间
                r = mid - 1
            mid = l + (r-l)//2
            # 当 mid 指向数组首尾两个元素时，为了满足数组为山脉数组，则峰值必定出现在第 2 个或者倒数第 2 个元素
            if mid == 0 or mid == nums_len - 1:
                mid = 1 if mid==0 else len - 2
                break
        
        '''
            step 2 判断 target 是否 超过 峰值
        '''
        # 走到这一步已经找到了山脉数组的峰值
        if mountain_arr.get(mid) < target:
            # 若数组峰值都小于目标值，则直接返回-1
            return -1

        '''
            step 3 上坡查找
        '''
        # 首个元素不大于 target 时，在峰值之前的递增区间内寻找 target 。 否则说明递增区间不存在 target
        if mountain_arr.get(0) <= target:
            # 左半部分递增区间内，l 指针指向0， r 指针指向峰值
            l = 0
            r = mid
            m = l+(r-l)//2
            while l <= r:
                # 递增区间内，若 中间值 小于 目标值，则往右半部分查找 目标值
                if mountain_arr.get(m) < target:
                    l = m+1
                # 递增区间内，若 中间值 大于 目标值，则往左半部分查找 目标值
                elif mountain_arr.get(m) > target:
                    r = m-1
                else:
                    # 中间值 等于 目标值，直接返回
                    return m
                m = l + (r-l)//2
        
        '''
            step 4 下坡查找
        '''
        # 最后一个元素不大于 target 时，在峰值之后的递减区间内寻找 target 。 否则说明递减区间不存在target
        if mountain_arr.get(nums_len-1) <= target:
            # 右半部分递减区间内， l 指针指向峰值， r 指针指向最后一个元素
            l = mid
            r = nums_len-1
            m = l+(r-l)//2
            while l <= r:
                # 递减区间内，若 中间值 小于 目标值，则往左半部分查找 目标值
                if mountain_arr.get(m) < target:
                    r = m-1
                # 递减区间内，若 中间值 大于 目标值，则往右半部分查找 目标值
                elif mountain_arr.get(m) > target:
                    l = m+1
                else:
                    # 中间值 等于 目标值，直接返回
                    return m
                m = l + (r-l)//2
        # 若存在target，则在上面两个判断已经return，走到这一步说明数组不存在 target
        return -1


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = [int(s) for s in str1.split(",")]
            target = int(str2)
            mountainArr = MountainArr(nums)
            res = solution.findInMountainArray(target,mountainArr)
            print(res)
        else:
            break

