'''
    287. 寻找重复数

    给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

    示例 1:

    输入: [1,3,4,2,2]
    输出: 2
    示例 2:

    输入: [3,1,3,4,2]
    输出: 3
    说明：

    不能更改原数组（假设数组是只读的）。
    只能使用额外的 O(1) 的空间。
    时间复杂度小于 O(n2) 。
    数组中只有一个重复的数字，但它可能不止重复出现一次。


'''
class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                return nums[i]
            i = i + 1

    def findDuplicate2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 1
        while i < len(nums):
            print(nums[i] ^ nums[i-1])
            if nums[i] ^ nums[i-1]==0:
                return nums[i]
            i = i + 1

    def findDuplicate(self, nums: List[int]) -> int:
        '''
            方法：快慢指针
            思路：
                1. 定义 双指针：slow（每次走一步），fast(每次走两步)
                2. step 1：找环
                3. step 2：第一次相遇，即都进入环中
                4. step 3：fast 归零
                5. step 4: fast 和 slow 每次都走一步，找再次相遇点
                6. step 5: 找到再次相遇点，即环入口
        '''
        slow = 0
        fast = 0
        # step 1：找环
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # step 2：第一次相遇，即都进入环中
            if slow==fast:
                # step 3：fast 归零
                fast = 0
                # step 4: fast 和 slow 每次都走一步，找再次相遇点
                while 1:
                    # step 5: 找到再次相遇点，即环入口
                    if slow==fast:
                        return slow
                    slow = nums[slow]
                    fast = nums[fast]
    
if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.findDuplicate(nums)
            print(res)
        else:
            break

