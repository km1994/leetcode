class Solution:
    def minNumber(self, nums: List[int]) -> str:
        '''
            # 题目：剑指 Offer 45. 把数组排成最小的数
            方法：快排
            解析：
                该问题 本身属于一个排序问题，但是与标准排序方法的区别在于 其 需要对 两个字符串 按不同的拼接顺序 进行 比较
                1. 若拼接字符串 x + y > y + x ，则 x “大于” y ；
                2. 反之，若 x + y < y + x ，则 x “小于” y ；
            思路：
                1. 将 数组 转化为 字符串；
                2. 修改 排序规则，利用 快排方法 进行 排序；
                3. 将排序后的结果 进行 破解
            复杂度：
                时间复杂度：O(NlogN)
                空间复杂度：O(N)
        '''
        strs = [str(num) for num in nums]
        self.quick_sort(strs, 0, len(strs) - 1)
        return ''.join(strs)

    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and key+array[right] < array[right]+key:
                right -= 1
            array[left] = array[right]
            while left < right and key+array[left] >= array[left]+key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)
    
    