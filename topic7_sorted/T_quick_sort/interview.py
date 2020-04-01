'''
   快排算法是如何实现的？

'''
class Solution:
    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] < key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] >= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums = [int(num) for num in str1.split(",")]
            solution.quick_sort(nums, 0,len(nums)-1)
            print(nums)
        else:
            break

