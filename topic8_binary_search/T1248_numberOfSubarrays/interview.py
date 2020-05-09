'''
    1248. 统计「优美子数组」

    给你一个整数数组 nums 和一个整数 k。

    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

    请返回这个数组中「优美子数组」的数目。

    示例 1：

    输入：nums = [1,1,2,1,1], k = 3
    输出：2
    解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
    示例 2：

    输入：nums = [2,4,6], k = 1
    输出：0
    解释：数列中不包含任何奇数，所以不存在优美子数组。
    示例 3：

    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
     
    提示：

    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length

'''
class Solution:
    def numberOfSubarrays(self, nums, k):
        res = 0
        nums_len = len(nums)
        left = 0
        right = 0
        oddCnt = 0
        while right < nums_len:
            # 右指针先走，每遇到一个奇数则 oddCnt+1。
            if nums[right]%2 == 1:
                oddCnt = oddCnt + 1
            right = right + 1

            # 若当前滑动窗口 [left, right) 中有 k 个奇数了，进入此分支统计当前滑动窗口中的优美子数组个数。
            if oddCnt == k:
                # 先将滑动窗口的右边界向右拓展，直到遇到下一个奇数（或出界）
                temp = right
                while right < nums_len and nums[right]%2 == 0:
                    right = right + 1
                
                # rightEvenCnt 即为第 k 个奇数右边的偶数的个数
                rightEvenCnt = right - temp

                # leftEvenCnt 即为第 1 个奇数左边的偶数的个数
                leftEvenCnt = 0
                while (nums[left]%2) == 0:
                    leftEvenCnt = leftEvenCnt + 1
                    left = left + 1

                # 第 1 个奇数左边的 leftEvenCnt 个偶数都可以作为优美子数组的起点
                # (因为第1个奇数左边可以1个偶数都不取，所以起点的选择有 leftEvenCnt + 1 种）
                # 第 k 个奇数右边的 rightEvenCnt 个偶数都可以作为优美子数组的终点
                # (因为第k个奇数右边可以1个偶数都不取，所以终点的选择有 rightEvenCnt + 1 种）
                # 所以该滑动窗口中，优美子数组左右起点的选择组合数为 (leftEvenCnt + 1) * (rightEvenCnt + 1)
                res = res + (leftEvenCnt+1)*(rightEvenCnt+1)

                # 此时 left 指向的是第 1 个奇数，因为该区间已经统计完了，因此 left 右移一位，oddCnt-1
                left = left + 1
                oddCnt = oddCnt - 1
        return res

                

        


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            nums = [int(num) for num in str1.split(",")]
            k = int(str2)
            res = solution.numberOfSubarrays(nums,k)
            print(res)
        else:
            break

