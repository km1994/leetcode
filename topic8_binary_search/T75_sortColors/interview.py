'''
   75. 颜色分类

   给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

    注意:
    不能使用代码库中的排序函数来解决这道题。

    示例:

    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]

'''
class Solution:

    # 哈希表
    def sortColors1(self, nums):
        '''
            问题分析：
                
            思路：
                
        '''
        countDict = {}
        for num in nums:
            if num not in countDict:
                countDict[num]= 1
            else:
                countDict[num] += 1
        
        res = []
        countList = sorted(countDict.items(), key = lambda item: item[0])
        for item in countList:
            res = res+[item[0]]*item[1]
        nums = res
        return nums

    # 双指针法
    def sortColors(self, nums):
        '''
            思路：
                初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.
                初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.
                初始化当前考虑的元素序号 ：curr = 0.
                While curr <= p2 :
                    若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
                    若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
                    若 nums[curr] = 1 ：将指针curr右移。
        '''
        left,cur = 0,0
        right = len(nums)-1
        while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left] = nums[left],nums[cur]
                cur = cur+1
                left = left+1
            elif nums[cur]==2:
                nums[cur],nums[right] = nums[right],nums[cur]
                right = right-1
            else:
                cur = cur+1
        return nums

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            res = solution.sortColors(nums1)
            print(res)
        else:
            break

