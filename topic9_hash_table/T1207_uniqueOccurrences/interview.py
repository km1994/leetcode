'''
    1207. 独一无二的出现次数

    给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

    示例 1：

    输入：arr = [1,2,2,1,1,3]
    输出：true
    解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
    示例 2：

    输入：arr = [1,2]
    输出：false
    示例 3：

    输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
    输出：true

'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 利用 字典 计数
        arr_dict = {}
        for a in arr:
            if a not in arr_dict:
                arr_dict[a] = 0
            arr_dict[a] += 1
        # 利用 集合 判重
        count_set = set()
        for key,val in arr_dict.items():
            if val not in count_set:
                count_set.add(val)
            else:
                return False
        return True
        
if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "":
            nums1 = [int(num) for num in str1.split(",")]
            res = solution.uniqueOccurrences(nums1)
            print(res)
        else:
            break

