'''
    239. 滑动窗口最大值

    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

    返回滑动窗口中的最大值。

    进阶：

    你能在线性时间复杂度内解决此题吗？

    示例:

    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7] 
    解释: 

    滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7
     
    提示：

        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        1 <= k <= nums.length

'''
import collections
class Solution:
    # 方法一：暴力法
    def maxSlidingWindow1(self, nums, k):
        res = []
        nums_len = len(nums)
        if nums_len < k:
            return res
        
        for i in range(0,nums_len-k+1):
            res.append(max(nums[i:i+k]))
        return res

    # 方法二：队列法
    def maxSlidingWindow(self, nums, k):
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            print()
            print(nums)
            print(f"num:{num}")
            # 从 队尾 将 超出 滑动窗 长度 的 元素 清除，使 队列 长度 小于等于 滑动窗
            while deque and deque[0] <= i - k: deque.popleft() # outdate indices
            # 保证 队尾 一定 是 滑动窗中 最大 元素
            while deque and num > nums[deque[-1]]: deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
            print(f"deque:{deque}")
            print(f"res:{res}")
        return res

      
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = [int(num) for num in str1.split(",")]
            k = int(str2)
            res = solution.maxSlidingWindow(nums, k)
            print(res)
        else:
            break

