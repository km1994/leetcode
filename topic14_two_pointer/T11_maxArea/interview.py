'''
   11. 盛最多水的容器

   给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

    示例：

        输入：[1,8,6,2,5,4,8,3,7]
        输出：49

'''
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            temp_area = min(height[l],height[r]) * (r-l)
            res = max(res,temp_area)
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return res


if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            res = solution.maxArea(nums)
            print(res)
        else:
            break

